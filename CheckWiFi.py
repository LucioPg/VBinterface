import os
import subprocess
import re
import winwifi
from time import sleep
from winwifi import WinWiFi as ww
import powershellmagic as psm


class CHECKWIFI(object):
    def __init__(self,netw=None):

        self.NOINTERFACES = "Nessuna interfaccia wireless nel sistema."
        self.INTERFACE = ""
        self.STATUSADAPTER = 0
        self.RIGHTNETWORK2 = "Vodafone-newstarsys"
        self.RIGHTNETWORK = "Vegeboard"
        # RIGHTNETWORK = "netest"
        self.NETWORKSAROUND = []
        self.SAMENET = False
        self.RESULTS = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("ISO-8859-1")

    def setRightNetwork2(self,network):
        network = self.RIGHTNETWORK2

    def refresh_RESULTS(self):
        self.RESULTS = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("ISO-8859-1")
        return self.RESULTS
    def checkWifi(self,netw):
        results = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
        # print(results)
        results = results.decode("ISO-8859-1")
        self.RESULTS = results
        if  self.NOINTERFACES in results:

            print("wifi non presente o disabilitato")
            print("risultati:\n ", results)
            interfaces = subprocess.check_output(["netsh","interface", "show", "interface"]).decode("ISO-8859-1")
            interfaces_lines = interfaces.split("\n")
            check = 0
            for i in interfaces_lines:
                if "Wi-Fi" in i:

                    check = 1
                    _i = i
            if check:
                print("questo è _i")
                print(_i.strip(" "))
                _i_lines = _i.split("  ")
                print(len(_i_lines))
                for x in _i_lines:
                    if "Wi-Fi" in x:
                        self.INTERFACE = _i_lines[_i_lines.index(x)]
                        print(self.INTERFACE)
                # checkWifi()
                return 1 #non ne sono molto sicuro
            else:
                print("nessuna interfaccia wifi trovata")
                return
        else:
            print("adattatore wifi rilevato\n")
            print("\n ", results)
            assert isinstance(results, str)
            self.INTERFACE = self.getAdapterName(results)
            print(self.INTERFACE)
            self.STATUSADAPTER = self.checkStatusAdapter(results)
            print(self.STATUSADAPTER)

        if self.STATUSADAPTER:
            # l=ww()
            # l.scan().decode("ISO-8859-1")
            print("ok, controllo che la Vegeboard sia a portata del tuo Wi-Fi")
            # checkNetwork(results)

            self.scanAround(netw)
        else:
            print("accensione radio Wi-Fi")
            self.toggleRadio()
            sleep(5)
            print("ok, controllo che la Vegeboard sia a portata del tuo Wi-Fi")
            self.scanAround(netw)
        # enable()

    def toggleRadio(self):
        from pathlib import Path
        filename = Path("{0}/tools/toggleWiFi.bat".format(os.getcwd()))

        if not filename.exists():
            print("Oops, file doesn't exist!")
            return
        toggle = subprocess.call([r'{0}'.format(filename)])
        print("toggle: ",toggle)


    def connect_to_network(self,netw):
        print("connessione a: ",netw)
        process = subprocess.Popen(
            'netsh wlan connect {0}'.format(netw),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        for i in stderr:
            print(i)


        # Return `True` if we were able to successfully connect
        return b'Connection request was completed successfully' in stdout

    def checkProfile(self,network):
        # connesso =subprocess.check_output("netsh wlan connect ssid=netest",shell=True)
        profili =winwifi.WinWiFi.get_profiles()
        # winwifi.WinWiFi.add_profile("./profilo)
        flag=0
        for x in profili:
            print(x)
            if network == x:
                print("profilo trovato, connessione in corso")
                flag = 1
                #connetti
                print(self.connect_to_network(network))
                self.SAMENET = True

        if not flag:

            print(subprocess.call('netsh wlan add profile filename="./profilerWIFI/Wi-Fi 2-Vegeboard.xml"'))
            sleep(5)
            self.SAMENET = False
            #bisogna aggiungere il profilo
        # print(profilo)
    def scanAround(self,netw):
        networks = subprocess.check_output(["netsh","wlan", "show", "networks"]).decode("ISO-8859-1")
        numeroRetiTrovate_split = networks.split("\n")
        numeroRetiTrovate_lst = []
        numeroRetiTrovate = ""
        networks = networks.split("\r\n")
        networks_lst = []
        # filtered = filter(lambda x: not re.match(r'^\s*$', x), networks)
        for j in numeroRetiTrovate_split:
            if not re.match(r'^\s*$', j):
                numeroRetiTrovate_lst.append(j.strip("\r\n"))
        for k in numeroRetiTrovate_lst[1]:
            if not k.isdigit():
                pass
            else:
                numeroRetiTrovate+=k
        numeroRetiTrovate = int(numeroRetiTrovate)
        # for i in networks:
        #     if not re.match(r'^\s*$', i):
        #         if i != " " and i != ":" and i != "":
        #             networks_lst.append(i)
        # print(numeroRetiTrovate_lst)
        print(numeroRetiTrovate)
        for i in numeroRetiTrovate_lst[::-1]:

            if i.startswith("SSID {0}".format(numeroRetiTrovate)):
                # print(i)
                self.NETWORKSAROUND.append(i.split(" : ")[1])
                # networks_lst.append(i)
                if numeroRetiTrovate >0 :
                    numeroRetiTrovate -=1
                else: break
        print('reti trovate ',self.NETWORKSAROUND)
        for r in self.NETWORKSAROUND:
            if netw == r:
                print("rete trovata, è ora di connettersi") ##vai ad un'altra funzione così posso usare questa funzione per scansionare le reti
                ##altra funzione
                self.checkProfile(netw)
                return
        else: print("rete non trovata")
    def checkNetwork(self,netw):
        results = self.refresh_RESULTS()
        results_lines = results.split("\n")
        flag = 0
        print("cerco la rete {0}".format(netw))
        for i in results_lines:
            if " SSID" in i:
                nomeRete_lines = i.split(" : ")
                nomeRete = nomeRete_lines[1].strip("  ").strip("\r")
                print(nomeRete)
                if nomeRete == netw:
                    print("sei nella rete della VB")
                    flag = 1
                    self.SAMENET = True
                    print("dalla funzione: ", self.SAMENET)
                    break
            else: self.SAMENET = False

        if not flag:
            print("SSID non corretta")
            print("controllo che la VB sia a portata della tua antenna Wi-Fi")
            self.SAMENET = False
            # scanAround(netw)
            return self.SAMENET
        else: return self.SAMENET



    def checkStatusAdapter(self,results):
        results_lines = results.split("\n")
        networkStatus = results_lines[9]
        connectionStatus = results_lines[7]
        for i in results_lines:
            print(results_lines.index(i),i)
            # nomeInterfaccia = results_lines[3]
            # if "Stato radio" in i:
            #
            #     # softwareStatus = results_lines[9]
            #     # connectionStatus = results_lines[7]
            #     # print("softwareStatus: ",softwareStatus)
            if "Stato" in connectionStatus:
                if "BSSID" in networkStatus:
                    self.STATUSADAPTER = 1
                    return self.STATUSADAPTER

                else:
                    print("wifi attivo ma non connesso")
                    self.STATUSADAPTER = 0
                    return self.STATUSADAPTER

            else:

                self.STATUSADAPTER = 0

                # print("attivare adattatore WI-Fi '%s' ?(S/N)" % INTERFACE)
                # return STATUSADAPTER



        return self.STATUSADAPTER

        # return 0


    def getAdapterName(self,results):
        results_lines = results.split("\n")

        for i in results_lines:
            # print(results_lines.index(i),i)
            # nomeInterfaccia = results_lines[3]
            if "Nome" in i:
                nome_lines = i.split(":")
                # print(nome_lines)
                if "\r" in nome_lines[1]:
                    # print("segnale \\r presente")
                    self.INTERFACE = nome_lines[1].strip("\r").strip(" ")
                else:
                    self.INTERFACE = nome_lines[1]
                # print(INTERFACE)
                # print("attivare adattatore WI-Fi '%s' ?(S/N)" % INTERFACE)
                return self.INTERFACE
        return 0

    def check_radio_on(self):
        # radio_status = subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","&Get-NetAdapter -Name WI* | fl status"])
        radio_status = subprocess.check_output(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","&Get-NetAdapter -Name WI* | fl status"]).decode("ISO-8859-1")
        radio_status = radio_status.split(":")[1]
        if "Up" in radio_status:
            return 1
        else:
            return 0
        # os.system("Get-NetAdapter -Name WI* | fl status")

    def enable(self):
        os.system("Get-NetAdapter")
        # os.system("netsh interface set interface 'Wi-Fi 2' enabled")

    def disable(self):
        print(os.system("netsh interface set interface 'Wi-Fi' disabled"))


# uncomment to start
# checkWifi()
# ISCONN = checkNetwork(RESULTS,RIGHTNETWORK)
# print(isconnected())