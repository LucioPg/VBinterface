#todo fare in modo che i suoni già presenti nella VB siano caricati in partenza (tip: usa il file defaultinstrument.ini sulla vb)



from PyQt5 import QtWidgets, QtCore, QtGui
from GUI import VB_Gui
import pickle
from GUI.dialog_salva_preset import Ui_Dialog_salva_preset as dialog_salva_preset
from GUI.VB_Gui_dialog_settings import Ui_Dialog_impostazioni
import time
import pysftp
import pickle
import os
from traceback import format_exc as fex
import paramiko
from CheckWiFi import CHECKWIFI
from tools.draggableItems_v2 import MyListWidgetItem, MyListWidget, DroppableLabel
from tools.QtWaitingSpinner.waitingspinnerwidget import QtWaitingSpinner, MySp
import sys
from collections import OrderedDict as odict
class VBInterface(VB_Gui.Ui_MainWindow,QtWidgets.QMainWindow):
    # VBADDRESS = "192.168.4.1"
    VBADDRESS = "192.168.1.15"
    RETE = "WebPocket-7873"
    PASSWD = "AL1LEIMI"
    LABEL_SIGNAL = QtCore.pyqtSignal(str)
    MTh_SIGNAL = QtCore.pyqtSignal()
    fileImpostazioni = 'conf.ini'
    def __init__(self,parent=None):
        super(VBInterface, self).__init__(parent)
        self.setupUi(self)
        self.corrispondenzaLabel = odict()
        self.setSpinner()
        self.labelDict =  odict()
        self.customWidget_instance()
        self.dizDaMandare = odict({x:'' for x in range(1,9)})
        self.strumentiPath = '/home/pi/Strumenti/'
        self.presetDict = {}
        self.defaultIni =odict()
        try:
            self.caricaImpostazioni()
        except:
            print(fex())
        self.mthread =  MThread(self.connectWifi)
        COLORS_A = ["background-color:rgba(0, 255, 0, 100);","background-color: rgba(255, 170, 0, 100);",
                    "background-color: rgba(255, 85, 0, 100);","background-color: rgba(85, 85, 255, 100);",
                    "background-color: rgba(255, 85, 255, 100);","background-color: rgba(255, 255, 0, 100);",
                    "background-color: rgba(170, 0, 0, 100);","background-color: rgba(200, 200, 200, 100);","background-color: rgba(255, 255, 255, 0);"]
        self.COLORS_B =[]
        for x in COLORS_A:
            y= [int(a) for a in x.split('(')[1].split(',')[:3]]
            alfa =  x.split('(')[1].split(',')[3].split(')')[0].strip(' ')
            y.append(int(alfa))
            self.COLORS_B.append(y)
        print('color_b ',self.COLORS_B)
        self.COLORS_A = COLORS_A
        NoCOLOR = COLORS_A[8]
        self.NoCOLOR = NoCOLOR
        COLORLIST_ALPHA = {self.label_slot_1: COLORS_A[0],
                           self.label_slot_2: COLORS_A[1],
                           self.label_slot_3: COLORS_A[2],
                           self.label_slot_4: COLORS_A[3],
                           self.label_slot_5: COLORS_A[4],
                           self.label_slot_6: COLORS_A[5],
                           self.label_slot_7: COLORS_A[6],
                           self.label_slot_8: COLORS_A[7],
                           "self.label_slot_1": COLORS_A[0],
                           "self.label_slot_2": COLORS_A[1],
                           "self.label_slot_3": COLORS_A[2],
                           "self.label_slot_4": COLORS_A[3],
                           "self.label_slot_5": COLORS_A[4],
                           "self.label_slot_6": COLORS_A[5],
                           "self.label_slot_7": COLORS_A[6],
                           "self.label_slot_8": COLORS_A[7]}
        COLORLIST_ALPHA_less = {self.label_slot_1: NoCOLOR,
                                self.label_slot_2: NoCOLOR,
                                self.label_slot_3: NoCOLOR,
                                self.label_slot_4: NoCOLOR,
                                self.label_slot_5: NoCOLOR,
                                self.label_slot_6: NoCOLOR,
                                self.label_slot_7: NoCOLOR,
                                self.label_slot_8: NoCOLOR,
                                "self.label_slot_1": NoCOLOR,
                           "self.label_slot_2": NoCOLOR,
                           "self.label_slot_3": NoCOLOR,
                           "self.label_slot_4": NoCOLOR,
                           "self.label_slot_5": NoCOLOR,
                           "self.label_slot_6": NoCOLOR,
                           "self.label_slot_7": NoCOLOR,
                           "self.label_slot_8": NoCOLOR}
        self.COLORLIST_ALPHA  = odict(COLORLIST_ALPHA)
        self.COLORLIST_ALPHA_less  = odict(COLORLIST_ALPHA_less)

        # self.ISCONN = self.checkWifi()


        self.wifi = CHECKWIFI()
        self.SAMENET = None
        self.lst_vb_dir = []
        self.dict_inst = {}
        self.cmd_answ = []
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshConnectStatus = False
        #todo sistemare proporzioni icona
        self.setWindowIcon(QtGui.QIcon('.\GUI\\_vb_interface_2.svg'))
        avoidClass = self.label_slot_5_dr.__class__
        print('avoiding ',avoidClass)
        la = [x for x in self.COLORLIST_ALPHA if type(x) is not str]
        nu = [x for x in range(1, 9)]
        # self.LABEL_LIST = odict({x: y for x, y in zip(nu, la)})
        self.LABEL_LIST = odict()
        counter = 0
        for xx in self.COLORLIST_ALPHA.keys():
            if type(xx) is not str:
                self.LABEL_LIST.setdefault(counter,xx)
            counter+=1
        print('label_list: ', self.LABEL_LIST)
        #setting signals
        self.MTh_SIGNAL.connect(self.stopSpinner)
        #setting buttons
        self.bot_salva_preset.clicked.connect(self.dialog_salva_preset)
        self.bot_applica.clicked.connect(self.applica)
        self.bot_pulisci.clicked.connect(self.pulisciDizDaMandare)
        self.bot_connetti.clicked.connect(self.connectWifi_container)
        self.bot_esci.clicked.connect(self.exit)
        self.bot_impostazioni.clicked.connect(self.dialog_settings)
        self.radio_hotSpot.toggled.connect(self.hs_switch)
        self.radio_hotSpot.setEnabled(False)
        self.bot_aggiungi.clicked.connect(self.addFile)
        ##setting combobox
        self.comboBox_strumenti.currentIndexChanged.connect(self.pop_lista_suoni)
        # self.radio_hotSpot.toggled.connect(self.connectSSH)
        # self.checkWifi()


        self.cleanAllLabels()


    def setSpinner(self):
        self.spinner_w = MySp(self.spinner)
        # self.spinner_w = QtWaitingSpinner(self.spinner)
        # self.spinner_w.setColor(color=QtCore.Qt.green)
        # self.spinner_w.setLineWidth(5.3)
        # self.spinner_w.setTrailFadePercentage(85)
        gridlay = QtWidgets.QGridLayout(self.spinner)
        self.spinner_w.setRevolutionsPerSecond(1.2)
        gridlay.addWidget(self.spinner_w)
        self.spinner.setLayout(gridlay)
        # self.spinner_w.start()
        self.spinner_w.stop()
    def applica(self):
        #temporaneo
        statusSpinner = self.spinner_w.isSpinning()
        if statusSpinner:
            self.spinner_w.stop()
            self.spinner_w.setColor(color=QtCore.Qt.lightGray)
        else:
            self.spinner_w.start()
            print(statusSpinner)

        print('applica: \n\t',self.dizDaMandare)

    def getPresetDict(self):
        pass
    def salvaPreset(self):
        # dovrebbe aprire una finesta per fare il salvataggio dei file
        check_flag = 0
        for i in self.presetDict.values():
            if i != '':
                check_flag +=1
        if check_flag == 0:
            print("nessun suono impostato")
            return
        file_save = QtWidgets.QFileDialog.getSaveFileName(self,'Salva Preset', 'VB_preset','Preset file (*.pst)')
        if file_save[0] != '':
            _= file_save[0].split('/')
            nome = _[-1]
            print(file_save)
            with open(nome, "wb") as f:
                pickle.dump(self.presetDict,f)
            print(nome)
        else:
            print("salvataggio preset annullato")
        return file_save

    def pulisciDizDaMandare(self):
        self.cleanAllLabels()
        for k in self.dizDaMandare:
            self.dizDaMandare[k] = ''
        print('Buffer suoni cancellato!')
        # print(self.dizDaMandare)
        return  self.dizDaMandare

    def setDizDaMandare(self,label,nomeFile):
        """
        prende il file dalla lista e la posizione dalle label
        :param label:
        :return:
        """

        print('nomeFile ',nomeFile)
        def num_fun(lab):
            for d in lab.objectName():
                if d.isdigit():
                    pos = int(d)
                    print('pos: ',pos)
                    return pos
                else:
                    pos = None
            print('pos is None')

            return 0
        pos = num_fun(label)
        if pos is 0:
            print('posizione non trovata in ',label.objectName())
            return

        print("name: {0} - {1}".format(pos,nomeFile))
        self.dizDaMandare[pos] = nomeFile
        return self.dizDaMandare
    def labCorrisponder(self,a,b):
        self.corrispondenzaLabel.setdefault(a,b)
        return self.corrispondenzaLabel

    def soundParser(self,s,mode,pos=1):

        sign = '@#-'
        if sign in s:
            _ss = s.split(sign)
            _s = _ss[1]
            if _ss[0].isdigit():

                pos = _ss[0]
            else:
                if _ss[0].startswith('/'):
                    pp = _ss[0].split('/')
                    pos = pp[-1]

                    pp.pop(int(pos))
                    path = '{}'.format(x for x in pp)
        else:
            _s = s
            pos = 9

        if mode == 'out':
            _s = '{0}'.format(str(pos)) + sign + s

        elif mode == 'out2':
            pass

        return _s, pos


    def customWidget_instance(self):
        # self.lista_suoni = QtWidgets.QFrame(self.centralwidget)
        self.lista_suoni_w = MyListWidget(self.lista_suoni)


        ## todo qui sotto c'è l'implementazione della stylesheet peccato che colora tutto di bianco invece che essere trasparente
        # ## per evitare il cambio di colore quando una riga è selezionata
        # self.lista_suoni_w.setStyleSheet("QListWidget::item:selected{background-color : transparent;}")
        #todo ############################################################


        self.lista_suoni_w.setMinimumSize(QtCore.QSize(191, 452))
        self.lista_suoni_w.setMaximumSize(QtCore.QSize(191, 452))
        item = MyListWidgetItem("lucio","Peppe",parent=self.lista_suoni_w)
        gridlay = QtWidgets.QGridLayout(self.lista_suoni)
        gridlay.addWidget(self.lista_suoni_w)
        self.lista_suoni.setLayout(gridlay)
        self.label_slot_5_dr = DroppableLabel(self.frame_svg_3)
        self.label_slot_5_dr.setText('cinque')
        # self.label_slot_5.setText('xxxxxxxxxxx')
        # print(type(self.label_slot_5_dr))
        self.label_slot_5_dr.setGeometry(QtCore.QRect(389, 153, 101, 91))
        self.label_slot_5_dr.DROPPED.connect(self.setLabel)
        self.labelDict.setdefault(self.label_slot_5_dr,'')
        self.labCorrisponder(self.label_slot_5_dr,self.label_slot_5)
        self.label_slot_5_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_5_dr.setObjectName("label_slot_5_dr")
        self.label_slot_1_dr = DroppableLabel(self.frame_svg_3)
        self.label_slot_1_dr.setText('uno')
        self.label_slot_1_dr.DROPPED.connect(self.setLabel)
        self.label_slot_1_dr.setGeometry(QtCore.QRect(80, 40, 101, 91))
        self.labelDict.setdefault(self.label_slot_1_dr, '')
        self.labCorrisponder(self.label_slot_1_dr,self.label_slot_1)
        self.label_slot_1_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_1_dr.setObjectName("label_slot_1_dr")
        self.label_slot_2_dr = DroppableLabel(self.frame_svg_3)
        self.labelDict.setdefault(self.label_slot_2_dr, '')
        self.labCorrisponder(self.label_slot_2_dr,self.label_slot_2)
        self.label_slot_2_dr.DROPPED.connect(self.setLabel)
        self.label_slot_2_dr.setGeometry(QtCore.QRect(250, 40, 101, 91))
        self.label_slot_2_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_2_dr.setObjectName("label_slot_2_dr")
        self.label_slot_3_dr = DroppableLabel(self.frame_svg_3)
        self.labelDict.setdefault(self.label_slot_3_dr, '')
        self.labCorrisponder(self.label_slot_3_dr,self.label_slot_3)
        self.label_slot_3_dr.DROPPED.connect(self.setLabel)
        self.label_slot_3_dr.setGeometry(QtCore.QRect(426, 40, 101, 91))
        self.label_slot_3_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_3_dr.setObjectName("label_slot_3_dr")
        self.label_slot_8_dr = DroppableLabel(self.frame_svg_3)
        self.labelDict.setdefault(self.label_slot_8_dr, '')
        self.labCorrisponder(self.label_slot_8_dr,self.label_slot_8)
        self.label_slot_8_dr .DROPPED.connect(self.setLabel)
        self.label_slot_8_dr.setGeometry(QtCore.QRect(424, 267, 101, 91))
        self.label_slot_8_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_8_dr.setObjectName("label_slot_8_dr")
        self.label_slot_7_dr = DroppableLabel(self.frame_svg_3)
        self.labelDict.setdefault(self.label_slot_7_dr, '')
        self.labCorrisponder(self.label_slot_7_dr,self.label_slot_7)
        self.label_slot_7_dr.DROPPED.connect(self.setLabel)
        self.label_slot_7_dr.setGeometry(QtCore.QRect(252, 268, 101, 91))
        self.label_slot_7_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_7_dr.setObjectName("label_slot_7_dr")
        self.label_slot_6_dr = DroppableLabel(self.frame_svg_3)
        self.labelDict.setdefault(self.label_slot_6_dr, '')
        self.labCorrisponder(self.label_slot_6_dr,self.label_slot_6)
        self.label_slot_6_dr.DROPPED.connect(self.setLabel)
        self.label_slot_6_dr.setGeometry(QtCore.QRect(80, 267, 101, 91))
        self.label_slot_6_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_6_dr.setObjectName("label_slot_6_dr")
        self.label_slot_4_dr = DroppableLabel(self.frame_svg_3)
        self.label_slot_4_dr.DROPPED.connect(self.setLabel)
        self.labelDict.setdefault(self.label_slot_4_dr, '')
        self.labCorrisponder(self.label_slot_4_dr,self.label_slot_4)
        self.label_slot_4_dr.setGeometry(QtCore.QRect(115, 152, 101, 91))
        self.label_slot_4_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_4_dr.setObjectName("label_slot_4_dr")

    def cleanAllLabels(self):
        """
        :return toglie il colore alle labels
        """
        self.frame_svg_3.blockSignals(True)
        lista = [self.label_slot_1_dr,self.label_slot_2_dr,self.label_slot_3_dr,self.label_slot_4_dr,self.label_slot_5_dr,
                 self.label_slot_6_dr,self.label_slot_6_dr,self.label_slot_7_dr,self.label_slot_8_dr]
        for c in range(1,9):
            w = self.frame_svg_2.findChild(QtWidgets.QLabel,"label_slot_{}".format(c))
            q = self.frame_svg_2.findChild(QtWidgets.QLabel,"label_slot_{}_dr".format(c))
            w.setStyleSheet("{}".format(self.COLORLIST_ALPHA_less[w]))
            w.setToolTip('')
            q.setToolTip('')
            q.setText('')
            w.setText('')
            q.repaint()
        for l in lista:
            # print(l.objectName())
            l.setText('')
            l.setToolTip('')
            # ind = c - 1
            # w.setStyleSheet("{}".format(lista[ind]))

        self.frame_svg_3.blockSignals(False)

    def dialog_salva_preset(self):
        dialog_salva = QtWidgets.QDialog()
        ui = dialog_salva_preset()
        ui.setupUi(dialog_salva)
        dialog_salva.exec_()
        nomeFile = ui.lineEdit.text()+'.prs'
        print('salvataggio in: ',nomeFile)
        with open(nomeFile,'wb') as f:
            pickle.dump(self.dizDaMandare,f)

        print(self.dizDaMandare)

    def setVBADD(self):
        self.dialog_settings.lineEdit.setText(self.VBADDRESS)

    def dialog_settings(self):
        self.Dialog_impostazioni = QtWidgets.QDialog()
        self.dialog_settings = dialog_settings()
        self.dialog_settings.setupUi(self.Dialog_impostazioni)
        self.dialog_settings.lineEdit.setText(self.VBADDRESS)
        self.dialog_settings.lineEdit_2.setText(self.RETE)
        self.dialog_settings.lineEdit_3.setText(self.PASSWD)
        if self.Dialog_impostazioni.exec_():
            indirizzo = self.dialog_settings.lineEdit.text()
            rete = self.dialog_settings.lineEdit_2.text()
            password = self.dialog_settings.lineEdit_3.text()
            if indirizzo != '':
                self.change_settings(mode='addr',addr=indirizzo)
            if rete != '':
                self.change_settings(mode='rete', rete=rete)
            if password != '':
                self.change_settings(mode='passw', passw=password)
            self.salvaImpostazioni(indirizzo, rete, password)

    def salvaImpostazioni(self, indirizzo, rete, password):
        lista = [indirizzo, rete, password]
        impostazioniStr = ''
        for i in lista:
            impostazioniStr +=str(i) + '\n'
        with open(self.fileImpostazioni, 'w') as f:
            f.write(impostazioniStr)

    def caricaImpostazioni(self):
        with open(self.fileImpostazioni, 'r') as f:
            impostazioniStr = f.readlines()
        print('caricaImpostazioni ************************', impostazioniStr)
        if len(impostazioniStr) == 3:
            self.VBADDRESS = impostazioniStr[0].strip('\n')
            self.RETE = impostazioniStr[1].strip('\n')
            self.PASSWD = impostazioniStr[2].strip('\n')
            print(self.RETE, self.PASSWD)
        else:
            print('ELSE: caricaImpostazioni ************************',impostazioniStr)

    def change_settings(self,mode='addr',addr='',rete='',passw=''):
        if mode == 'addr':
            self.VBADDRESS = addr
            print("VBADDRESS has changed",self.VBADDRESS)
            return self.VBADDRESS
        elif mode == 'rete':
            self.RETE = rete
            print("rete has changed", self.RETE)
            return  self.RETE
        elif mode == 'passw':
            self.PASSWD = passw
            print("PASSWD has changed", self.PASSWD)
            return self.PASSWD

    def commandSSH(self,cmd):
        _cmd = cmd
        self.cmd_answ.clear()
        try:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            for line in stdout:
                self.cmd_answ.append(line.strip('\n'))
                # print(line.strip('\n'))
        except AttributeError:
            try:
                self.connectSSH(1)
                self.commandSSH(_cmd)
                self.ssh.close()
                return stdout
            except:
                print("failed in commandSSH")
                return 0
        return self.cmd_answ

    def connectSSH(self,mode):
        if mode == 1:
            addr = "192.168.4.1"
            print('connessione all\'indirizzo: ',addr)
            self.ssh.connect(hostname="192.168.4.1", username="pi", password="ciao",timeout=2000)
        else:
            addr = "192.168.1.15"
            print('connessione all\'indirizzo: ',addr)
            self.ssh.connect(hostname="192.168.1.15", username="pi", password="ciao",timeout=2000)
        #

    def hs_switch(self):
        if self.isconnected():
            self.connectSSH(1)
            # b=self.commandSSH('dir Strumenti')
            # for line in b:
            #     print(line)
            #
            self.getVBfiles()
        print("stato connessione wifi: ", self.SAMENET)

    def getVBfiles(self,path=None):
        """Ritorna un dizionario che serve per popolare la lista dei suoni
        e la combobox con gli strumenti"""
        defaultIniPath = '/home/pi/scripts/touchHat/defaultStrum.ini'
        if path is None:
            path = '/home/pi/scripts/touchHat/' \
                   'SuoniVari/'

        self.dict_inst.clear()
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        if path is not None:
            with pysftp.Connection(self.VBADDRESS, username='pi', password='ciao', cnopts=cnopts) as sftp:
                defaultIni = sftp.get(defaultIniPath)
                with open('./defaultStrum.ini',"rb") as f:
                    self.defaultIni = pickle.load(f)
                print('got defaultIni: \n',self.defaultIni)
                sftp.chdir(path)
                for file in sftp.listdir():
                    # print(file)
                    if sftp.isdir(file):
                        a = []
                        self.dict_inst.setdefault(file,a)
                for k in self.dict_inst.keys():
                    newpath = pysftp.reparent(path,k)
                    # print('reparent: ',newpath)
                    sftp.chdir(newpath)
                    for inst in sftp.listdir():
                        self.dict_inst[k].append(inst)

            # print('self.dict_inst: ',self.dict_inst)
            return self.dict_inst, self.defaultIni
        else: return

    def addFile(self):
        # todo se connesso self.sshConnectStatus == True
        dialog, _ = QtWidgets.QFileDialog().getOpenFileNames(filter='*.wav')
        try:
            print(dialog)
            print(QtCore.QUrl().fromLocalFile(dialog[0]))
            self.commandSSH()
        except:
            print(fex())

        # if dialog.exec_():
        #     try:
        #         nomeFile = dialog.fileSelected()
        #         print('FILE SELECTED: ', nomeFile)
        #     except: print(fex())

    @QtCore.pyqtSlot(QtWidgets.QLabel,str)
    def setLabel(self,lab,txt,item=None):
        # txt sarà il nome del file
        # print('oggetto label: ',lab)
        print('il famoso txt: ',txt)
        self.labelDict[lab.objectName()] = txt
        pos=0
        noColor = QtGui.QColor(self.COLORS_B[-1][0],self.COLORS_B[-1][1],self.COLORS_B[-1][2],self.COLORS_B[-1][3])
        for x in lab.objectName():
            if x.isdigit():
                pos = int(x)
                if pos > 0:
                    pos-=1
                else:
                    pos = 0
                break
        brush = QtGui.QBrush()
        brush.setStyle(QtCore.Qt.SolidPattern)
        if item is None:
            itemLista = self.lista_suoni_w.currentItem()
        else:
            itemLista = item

        # print('setLabel for list: ',itemLista.text())
        # print('setLabel for index: ',pos)
        # print("label: {0} set: {1}".format(lab.obje0ctName(),txt))
        if txt == '':
            print("{} vuota".format(lab.objectName()))
            self.corrispondenzaLabel[lab].setStyleSheet(self.COLORLIST_ALPHA_less[self.corrispondenzaLabel[lab]])
            brush.setColor(noColor)

        else:
            print("{0} {1}".format(lab.objectName(),self.labelDict[lab.objectName()]))
            try:
                print("changing for: {0} in {1}".format(self.corrispondenzaLabel[lab].objectName(),self.COLORLIST_ALPHA[self.corrispondenzaLabel[lab]]))
                brush.setColor(QtGui.QColor(self.COLORS_B[pos][0], self.COLORS_B[pos][1], self.COLORS_B[pos][2],
                                            self.COLORS_B[pos][3]))
                self.corrispondenzaLabel[lab].setStyleSheet(self.COLORLIST_ALPHA[self.corrispondenzaLabel[lab]])
            except KeyError:
                print("TENTATIVO #2 ----- changing for: {0} in {1}".format(lab.objectName(),
                                                        self.COLORLIST_ALPHA[lab]))
                brush.setColor(QtGui.QColor(self.COLORS_B[pos][0], self.COLORS_B[pos][1], self.COLORS_B[pos][2],self.COLORS_B[pos][3]))
                lab.setStyleSheet(self.COLORLIST_ALPHA[lab])
        # for c in self.dizDaMandare.values():
        #     print(c)
        if itemLista is not None:
            itemLista.setBackground(brush)


    def loadColorLabels(self,inst,path,pos,item):
        suoni=[x for x in self.defaultIni['strumenti'][inst]]
        # _pos = len(suoni)+1
        # brush = QtGui.QBrush()
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # for pos in range(1,_pos):
        pos = int(pos)+1
        if pos < 8:
            lab = self.LABEL_LIST[pos]
            self.setLabel(lab,path,item=item)
        # brush.setColor(QtGui.QColor(self.COLORS_B[pos][0], self.COLORS_B[pos][1], self.COLORS_B[pos][2],
        #                                     self.COLORS_B[pos][3]))
        # lab.setStyleSheet(self.COLORLIST_ALPHA[lab])
        #



    def pop_lista_suoni(self,v=0):
        self.lista_suoni_w.clear()
        listaStrumenti = self.defaultIni['strumenti']
        if v is not None:
            strum = self.comboBox_strumenti.itemText(v)

            for s in self.dict_inst[strum]:
                _s,pos = self.soundParser(s, mode='in')
                # sp = self.soundParser(s,mode='out',pos=pos)[0]
                path = self.strumentiPath+strum+'/'+s
                item = MyListWidgetItem(_s, path, parent=self.lista_suoni_w)
                if strum in listaStrumenti:
                    # print('ehi {} è nella lista di default!'.format(strum))
                    self.loadColorLabels(strum,path,pos,item)
                    # self.setLabel()

        pass


    def pop_combo_strum(self):
        items = self.dict_inst
        # print('self.dict_inst: ',self.dict_inst)
        # print('items: ',items)
        self.comboBox_strumenti.blockSignals(True)
        self.comboBox_strumenti.clear()
        default=0
        listaStrumenti = self.defaultIni['strumenti']
        counter = 0
        for v in items:
            self.comboBox_strumenti.addItem(v)


        self.comboBox_strumenti.setCurrentIndex(default)
        self.comboBox_strumenti.blockSignals(False)

    def isconnected(self):
        self.SAMENET = self.wifi.checkNetwork(self.wifi.RIGHTNETWORK)
        return self.SAMENET
    def exit(self):
        self.close()
    def checkWifi(self):
        if self.SAMENET:
            self.radio_hotSpot.setEnabled(True)
            self.bot_aggiungi.setEnabled(True)
            self.bot_nuovaCartella.setEnabled(True)
            self.bot_rimuovi.setEnabled(True)
            self.bot_pulisci.setEnabled(True)
            self.bot_connetti.setEnabled(False)
            self.tabWidget.setTabEnabled(0,True)
        else:
            self.radio_hotSpot.setEnabled(False)
            self.bot_aggiungi.setEnabled(False)
            self.bot_nuovaCartella.setEnabled(False)
            self.bot_rimuovi.setEnabled(False)
            self.bot_pulisci.setEnabled(False)
            self.tabWidget.setTabEnabled(0, False)
            self.bot_connetti.setEnabled(True)

    @QtCore.pyqtSlot()
    def stopSpinner(self):
        print('spinner stopped')
        self.spinner_w.stop()

    def connectWifi_container(self):
        self.spinner_w.start()
        self.mthread.start()
    def connectWifi(self):
        print("clicked")

        try:
            self.getVBfiles()
            self.pop_combo_strum()
            self.pop_lista_suoni()
            self.caricaDefaultini()
            self.sshConnectStatus = True
            self.spinner_w.setMyColor(QtCore.Qt.darkGreen)
            self.spinner_w.setColor(self.spinner_w.baseColor)
            self.spinner_w.update()
            print('colore spinner: ',self.spinner_w.baseColor)
            print('status connessione: ', self.sshConnectStatus)
        except paramiko.ssh_exception.SSHException:

            a = self.wifi.scanAround(self.wifi.RIGHTNETWORK2)
            self.SAMENET = self.wifi.checkNetwork(self.wifi.RIGHTNETWORK2)
            print('non connesso con la VB')
            self.sshConnectStatus = False
            self.spinner_w.setMyColor(QtCore.Qt.darkRed)
            self.spinner_w.setColor(self.spinner_w.baseColor)
            self.spinner_w.update()
            print('colore spinner: ', self.spinner_w.baseColor)
            print('status connessione: ', self.sshConnectStatus)
        # self.spinner_w.stop()
        self.MTh_SIGNAL.emit()

        return self.sshConnectStatus
        # print(a.ISCONN)
    def caricaDefaultini(self):
        if 'strumenti' in self.defaultIni:
            for v in self.defaultIni['strumenti']:
                if self.defaultIni['strumenti'][v]['default']:
                    print('questo è lo strumento di deafault: ',v)

class dialog_settings(Ui_Dialog_impostazioni):
    def __init__(self):
        super(dialog_settings, self).__init__()
    def onExit(self):
        pass

class MThread(QtCore.QThread):
    def __init__(self,fun):
        QtCore.QThread.__init__(self)
        self.connessione = fun

    def __del__(self):
        self.wait()

    def run(self):
        self.connessione()

# class myfiles(QtWidgets.QFileSystemModel):
#     def __init__(self):
#         super(myfiles, self).__init__()
#
#     def columnCount(self, parent=None, *args, **kwargs):
#         ###override per ridurre il numero di colonne da 4 a 1
#         return 1
# class mylabel(QtWidgets.QLabel):
#     def __init__(self):
#         super(mylabel, self).__init__()
#         self.acceptDrops(True)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VBInterface()
    ui.show()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())