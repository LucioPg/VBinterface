import paramiko
import sys
import traceback
import pysftp
from functools import wraps
from PyQt5 import QtCore, QtWidgets
import json
import time
#import creation_date

# class conSSH(object):
from pyasn1.codec.der.encoder import encode


class conSSH(QtCore.QObject):
    # commandToSend = "rm *.dat"
    risultatoRicerca = {}
    # risultatoRicerca = []
    conn = False
    # commandToSend = "dir /datBa/"
    commandToSend = "cat /etc/hostname"
    # commandToSend = "dir"
    transSignal = QtCore.pyqtSignal(str)
    listaFout = []
    aliasName = ''
    def __init__(self,hostname='192.168.4.1',username=None,password=None,addr=None, local = None, privato=bool, listaExt=None):
        super(conSSH, self).__init__()
        self.listaExt = listaExt
        self.username = username
        self.password = password
        self.hostname = hostname
        self.fileIn, self.fileOut, self.fileErr =sys.stdin,sys.stdout,sys.stderr
        self.localAddr = local
        self.privato = privato
        self.magnetFlag = False
        self.countRif = 0


        try:
            self.torrName = self.getTorrName()
            # print('torrent name:',self.torrName)
            if self.torrName.startswith('magnet:'):
                # print('comincia con magnet!!!!!!!!!!')
                self.addr = addr
                self.magnetFlag = True
            else:
                self.addr = addr+self.torrName
                self.magnetFlag = False

            # self.addr = addr
            # print('host:',self.hostname)
            # print('user: ',self.username)
            # print('password',self.password)
            # print('destinazione:',self.addr)
        # try:
        #     self.addr_2 = addr+self.torrName
        #     print('destinazione2:', self.addr_2)
        #
        except:
            # print('addr',self.addr)
            # print('torr',self.torrName)
            pass
            # print(traceback.format_exc())
    def decoDebug(func):
        """decoratore: fornisce supporto traceback"""
        @wraps(func)
        def inside(inst,*args, **kwargs):
            try:
                print('nome della funzione: ',func.__name__)
                try:
                    return func(inst,*args,**kwargs)
                except:
                    return func(*args,**kwargs)
            except:
                print(traceback.format_exc())
        return inside

    def decoTime(func):
        """decorstore: per misurare quanto ci mette una funzione"""
        @wraps(func)
        def inside(inst,*args, **kwargs):
            t0 = time.time()
            func(inst,*args,**kwargs)
            t1 = time.time()
            tz = round(t1-t0,2)
            print('tempo "{}": {} sec'.format(func.__name__,tz))
        return inside
    def getAliasName(self, a):

        self.aliasName = a[0]
        # print('get alias /etc/hostname ', a[0])
        return self.aliasName
    def getTorrName(self):
        try:
            if self.localAddr is not None:
                if len(self.localAddr) == 0:
                    print('sembra vuoto: ', self.localAddr)
                    return None
                else:
                    s = self.localAddr.split('\\')
                    return s[-1]

            else:
                pass
        except:
            print(traceback.format_exc())
            pass
    def setCommand(self,c):
        self.commandToSend = c
        return self.commandToSend
    def setConn(self,b):
        self.conn = b
        return self.conn
    def execCommand(self):
        if self.conn:
            fileIn, fileOut, fileErr = self.ssh_client.exec_command(self.commandToSend)
            # print("risposta: ",fileOut)
            # print('errore: ',fileErr)
            self.ssh_client.close()
            self.setConn(False)
            return fileOut, fileErr

        else:
            self.startClient()
            fileIn, fileOut, fileErr = self.ssh_client.exec_command(self.commandToSend)
            # print("risposta: ",fileOut)
            # print('errore: ',fileErr)
            self.ssh_client.close()
            self.setConn(False)
            return fileOut, fileErr

    def listaFileDirectory(self):
        pass


    # with pysftp.Connection('192.168.1.200', username='lucio', password='ciaociao83') as sftp:
    #     sftp.remote_server_key
    def p1(self,f):
        lines = ''
        if self.listaExt is not None and len(self.listaExt) > 0:
            for e in self.listaExt:
                if f.endswith(e):
                    try:
                        _ff = f.replace(' ', '\ ')
                        ff = _ff.replace('(', '\(')
                        ff = ff.replace(')', '\)')
                        ff = ff.replace('\'', '\\\'')
                        ff = ff.replace('&', '\&')
                        ff = ff.replace('$', '\$')

                        # print('++++++++, ', ff)
                        fout, ferr = self.startClient('stat {}'.format(ff))
                        # _fout= self.ssh_client.exec_command('stat {}'.format(f))
                        # print(type(_fout[1]), len(_fout),'tipo _fout')
                        # fout = _fout[0].readlines()
                        # ferr = _fout[1]
                        lines = fout.readlines()
                        # print(lines)
                        if len(lines) == 0:
                            print('ferr: ', ferr.readlines())
                            print('fout: ', f)
                        else:
                            last = lines[6].split('Cambio   :')
                            last = last[1]
                            last = last.split('+')[0]
                            dim = lines[1].strip(' ')
                            dim = dim.split(' ')[1]
                            dim = dim.split('\tBlocchi')[0]
                            # dim = dim.strip(' ')
                            # dim = dim.strip('\t')[0]


                            if lines[-1] == 'Creazione: -\n':
                                created = last
                            else:
                                created = lines[-1]
                        # s = f.split(self.path)[1]
                        # _s = s.replace('/','\\')
                        #
                        # _f = '\\\\192.168.1.200\\'+_s
                        # print(_f)
                        # # last, created = creation_date.creation_date(_f)
                        # last, created = creation_date.creation_date_2(_f)
                        # print('last',last)
                    except:
                        lines = ''
                        print(traceback.format_exc())
                    t = self.parseRisultatoServer(f)
                    nome = t[0]
                    ext = t[1]
                    tags = self.tagger(t,mode='server')
                    if f not in self.risultatoRicerca.keys():
                        self.risultatoRicerca.setdefault(f, {'nm':nome, 'ext':ext,'tags':tags,'last':last,'created':created,'dim':dim,'acta':f,'lock':False,'rating':(0,0,False)})
                        # print('{} aggiunto'.format(nome))
                        break
                    # if f not in self.risultatoRicerca.keys():
                    #     self.risultatoRicerca.setdefault(f,(nome,ext,tags,last,created,dim))
                    else:

                        oldLast = self.risultatoRicerca[nome]['last']
                        oldDim = self.risultatoRicerca['nome']['dim']
                        if oldDim>=dim:
                            break
                        if last > oldLast:
                            self.risultatoRicerca.setdefault(nome, {'nm': nome, 'ext': ext, 'tags': tags, 'last': last,
                                                                    'created': created, 'dim': dim, 'acta': f,
                                                                    'lock': False, 'rating': (0, 0, False)})
                            self.risultatoRicerca.setdefault(f, (nome, ext, tags, last, created,dim))
                            print('sostituzione copia di ',t[0])
                        else:
                            print('copia non sostituita')
                        break
        else:
            print('sono p1 else connectSSh')
            pass
            # if f not in self.risultatoRicerca:
            #     self.risultatoRicerca.append(f)
        # print('risultato: ',len(self.risultatoRicerca))
        # if len(lines) == 0:
        #     pass
        # else:
        #
        #     print('lettura di stat: ','\n',lines)
        # print('lettura di stat: \n',self.listaFout[-1].readlines())
        return self.risultatoRicerca



    def parseRisultatoServer(self,risultato):
        try:
            root = self.path
            # print('root',self.dirPath)
        except:
            print('ME NE TORNO')
            return
        lista = []
        def estraiExt(nomefile):
            r = nomefile[::-1]
            _nomeR = r.split('.',1)
            ext = _nomeR[1][::-1]
            nome = '.' + _nomeR[0][::-1]
            return nome, ext

        def splitta(cosa, con=None):
            # print('cosa',cosa)
            if con is None:
                con = '/'
                conW = '\\'
                if con in cosa:
                    s = cosa.split(con)
                elif conW in cosa:
                    s = cosa.split(conW)
                else:
                    s = cosa
                    print('qualcosa non torna ',type(s))
                try:
                    file = s.pop(-1)
                except AttributeError:
                    print('AttributeError')
                    file = s[:-4]
                resto = s
                return file, resto
            else:
                pass
                # if con in cosa:
                #     s = cosa.split(con)
                #     nome, ext = estraiExt(s[-1])
                # return nome, ext

        # for _r in risultato:
            ##### todo da modificare in caso si vogliano inserire più percorsi in cui cercare
        if root in risultato:
        # if root in _r:
            r_ = risultato.replace(root,'')
            # r_ = _r.replace(root,'')

            # print('root in _r',r_)
            c, cr = splitta(r_)
            ext, nome = estraiExt(c)
            t = (nome,ext,cr)
            lista.append(t)
            return t

        else:
            # lista.append(splitta(_r))

                print(root,'<<<<>>>',risultato,'--------',lista)
        # return lista

    def setPath(self,p):
        self.path = p
        return self.path
    def setAddr(self,addr):
        self.addr = addr
        return self.addr

    @decoTime
    def wTree(self,path=None):
        print('lista ext ',self.listaExt)
        self.startClient()
        if path is None:
            # path = '/srv/dev-disk-by-label-intehdd/interno/'
            # path = '/srv/dev-disk-by-label-intehdd/interno/incomplete/'
            path = '/home/pi/Strumenti'

        self.setPath(path)


        def p2(f):
            pass
            # l = []
            # if f not in l:
            #     print('222222',f)
            #     l.append(f)
            return None

        def p3(f):
            pass
            # l = []
            # if f not in l:
            #     print('333333',f)
            #     l.append(f)
            return None
        self.risultatoRicerca.clear()
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection('192.168.4.1', username='pi', password='ciao', cnopts=cnopts) as sftp:
            sftp.walktree(path, self.p1, p2, p3)
        print('risultato: ', len(self.risultatoRicerca))
        return False

    def tagger(self, nomefile, mode = None):
        taglist = []
        esclusi = ['.com', '_', '.', "'", ',', '.net', '.org', 'wwww.','(',')','{','}']
        if mode == 'server':
            t = nomefile[-1]
            _tags = set(t)
            _taglist = list(_tags)
            taglist = [x.lower() for x in _taglist]
            for tg in taglist:
                if tg in esclusi or len(tg)<2:
                    taglist.remove(tg)
            e = nomefile[1]
            nomefile = nomefile[0]

        for es in esclusi:
            if es in nomefile:
                nomefile = nomefile.replace(es, ' ')
        _nm = nomefile.split(' ')
        for tag in _nm:
            if len(tag) > 2 and tag.lower() not in taglist:
                taglist.append(tag.lower())
            else:
                pass
        if mode == 'server':
            return taglist
            # return taglist, nomefile, e
        else:
            return taglist
    def startClient(self,command=None):
        if command is None:
            command = self.commandToSend
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # try:
        #     self.ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)
        #     print('vediamo: ')
        #     print('vediamo: ')
        #     print('vediamo: ')
        #     # fileIn, fileOut, fileErr = self.ssh_client.exec_command("cd /srv/dev-disk-by-label-mainUsb/gamesAndCo", )
        #     # fileIn, fileOut, fileErr = self.ssh_client.exec_command("echo $PATH")
        #     try:
        #         fileIn, fileOut, fileErr = self.ssh_client.exec_command(self.commandToSend)
        #         # fileIn, fileOut, fileErr = self.ssh_client.exec_command("rm *")
        #         # fileIn, fileOut, fileErr = self.ssh_client.exec_command("rm *")
        #     except:
        #         import traceback
        #         print(traceback.format_exc())
        #
        #     print(fileOut.readlines())
        #     print('fileErr:', fileErr.readlines())
        #     print('fileOut:', fileOut.readlines())
        # except paramiko.ssh_exception.AuthenticationException:
        #     print('autenticazione fallita')
        # self.ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)
        self.ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)
        self.setConn(True)
        # fileIn, fileOut, fileErr = self.ssh_client.exec_command("cd /srv/dev-disk-by-label-mainUsb/gamesAndCo", )
        # fileIn, fileOut, fileErr = self.ssh_client.exec_command("echo $PATH")
        try:
            fileIn, fileOut, fileErr = self.ssh_client.exec_command(command)
            # print('dal modulo ',fileOut.readlines())
            # self.ssh_client.close()
            if command == "cat /etc/hostname":
                self.getAliasName(fileOut.readlines())

            return fileOut, fileErr
            pass
            # fileIn, fileOut, fileErr = self.ssh_client.exec_command("rm *")
            # fileIn, fileOut, fileErr = self.ssh_client.exec_command("rm *")
            # fileIn, fileOut, fileErr = self.ssh_client.exec_command('dir')
            # fileIn, fileOut, fileErr = self.ssh_client.exec_command("rm *")
            # fileIn, fileOut, fileErr = self.ssh_client.exec_command("rm *")
            # print('dal modulo ', fileOut.readlines())
        except:
            pass


        # self.ssh_client.close()

    def printTotals(self,transferred, toBeTransferred):
        Old_stringa = "Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred)
        perc = ((transferred + 1 )/ toBeTransferred)*100
        perc = round(perc,2)
        stringa = 'Trasferimento: {}%'.format(perc)
        self.transSignal.emit(stringa)

    def getFile(self,filename):
        sftp = self.ssh_client.open_sftp()
        remote_file = sftp.open(filename)
        db = remote_file
        # db = json.loads(_db).read()

        # db = json.loads(remote_file).read()
        # sftp.close()


        # db = remote_file.readlines()
        return db
    def spedisciArchivio(self,nome):
        file = '/datBa/datBa_{}.json'.format(nome)
        # file = '/datBa/datBa.json'.format(nome)
        local = 'datBa_{}.json'.format(nome)
        # local = 'C:\\Users\Lucio\PycharmProjects\piserver_py\\testers\creaz_archivio\Megarch\MegaArch_3\datBa_generale.json'

        try:
            sftp = self.ssh_client.open_sftp()
            sftp.put(local, file, callback=self.printTotals)
            sftp.close()

            self.ssh_client.close()
        except:
            print(traceback.format_exc())
            self.startClient()
            sftp = self.ssh_client.open_sftp()
            sftp.put(local, file, callback=self.printTotals)
            sftp.close()

            self.ssh_client.close()

    def sendFile(self,local=None,add=None):

        if local is None:
            localAddr = self.localAddr
        else:
            localAddr = local
        if add is None:
            addre = self.addr
        else:
            addre = add
        try:
            if not self.privato:
                if not self.magnetFlag:
                    sftp = self.ssh_client.open_sftp()
                    # scrivere qui il percorso del file da esportare via ssh
                    # percorsoLocale = "C:\\Users\Grim\PycharmProjects\piserver_py\pinotify.py"
                    # percorsoRemoto = "/srv/dev-disk-by-label-serverhdd/clone1/pirata/scripts/pinotify.py"
                    # sftp.put(self.localAddr, self.addr)
                    sftp.put(localAddr, addre,callback=self.printTotals)
                    sftp.close()
                    self.setCommand("transmission-remote -n '{}:{}' -a {}".format(self.username, self.password, self.addr))
                    self.execCommand()
                    self.ssh_client.close()
                    self.setConn(False)
                else:
                    self.setCommand("transmission-remote -n '{}:{}' -a {}".format(self.username, self.password, self.torrName))
                    self.execCommand()
                    self.ssh_client.close()
                    self.setConn(False)
            else:
                if not self.magnetFlag:
                    sftp = self.ssh_client.open_sftp()
                    # scrivere qui il percorso del file da esportare via ssh
                    # percorsoLocale = "C:\\Users\Grim\PycharmProjects\piserver_py\pinotify.py"
                    # percorsoRemoto = "/srv/dev-disk-by-label-serverhdd/clone1/pirata/scripts/pinotify.py"
                    # sftp.put(self.localAddr, self.addr)
                    sftp.put(localAddr, addre,callback=self.printTotals)
                    sftp.close()
                    self.ssh_client.close()
                    self.setConn(False)
                else:

                    self.setCommand(
                        " deluge-console -c /home/gep/deluge-daemon/.config/deluge add {}".format(self.torrName))
                        # "transmission-remote -n '{}:{}' -a {}".format(self.username, self.password, self.torrName))
                    self.execCommand()
                    # self.setCommand('add {}'.format(self.torrName))
                    # self.execCommand()
                    self.setCommand('exit')
                    self.execCommand()
                    self.ssh_client.close()
                    self.setConn(False)
        except:
            print(traceback.format_exc())
            return False

    def invertiSlash(self,url):
        b = url.replace('/','\\')



if __name__ == '__main__':
    c = conSSH(username='pi',password='ciao',addr='/home/pi',local='C:\\Users\Lucio\Desktop\\atlas\VBinterface\VBinterface\\note\\note_rasp')
    c.startClient()
    # c.sendFile()