###
# listwidget con items draggabili in labels


from PyQt5 import QtGui, QtCore, QtWidgets
import sys, os


class MyListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self, label, data, parent=None):
        super(QtWidgets.QListWidgetItem, self).__init__(label, parent=parent)
        self.data = data

    def GetData(self):
        return self.data


class MyListWidget(QtWidgets.QListWidget):
    def __init__(self,parent=None):
        super(MyListWidget, self).__init__(parent)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(False)
        self.viewport().setAcceptDrops(False)
        self.setDropIndicatorShown(True)
        # self.setStyleSheet("QListWidget { background-color: rgb(0, 255, 0)}")


    def startDrag(self, supportedActions):
        drag = QtGui.QDrag(self)
        t = [self.selectedItems()[-1].GetData()]  # in questo modo passo solo l'ultimo selez in caso di selez multipla
        # t = [i.GetData() for i in self.selectedItems()]
        mimeData = self.model().mimeData(self.selectedIndexes())
        mimeData.setText(str(t))
        drag.setMimeData(mimeData)
        if drag.exec_(QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            pass
            # for item in self.selectedItems():
            #     self.takeItem(self.row(item))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        else:
            event.accept()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        else:
            event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        if isinstance(event.source(), MyListWidget):
            event.setDropAction(QtCore.Qt.MoveAction)
            super(MyListWidget, self).dropEvent(event)
        else:
            event.ignore()

    def dropMimeData(self, index, mimedata, action):
        super(MyListWidget, self).dropMimeData(index, mimedata, action)
        return True


class DroppableLabel(QtWidgets.QLabel):
    # DROPPED = QtCore.pyqtSignal(str)
    DROPPED = QtCore.pyqtSignal(QtWidgets.QLabel,str)
    TXT_CHANGED = QtCore.pyqtSignal(str)
    PRIMA = ''
    ORA = ''
    def __init__(self, parent):
        super(DroppableLabel, self).__init__(parent)
        # QtWidgets.QLabel.__init__(self, txt, parent)
        # self.setStyleSheet("QLabel { background-color: rgb(255, 255, 0)}")
        self.setAcceptDrops(True)
        # self.textChanged.connect(self.prova)
        # self.DROPPED.connect(self.prova)
        self.TXT_CHANGED.connect(self.textChanged)

    @QtCore.pyqtSlot(str)
    def textChanged(self,ora):
        self.ORA = ora
        if self. PRIMA != self.ORA:
            self.PRIMA = self.ORA
            self.ORA = ora
            self.DROPPED.emit(self,ora)
            print(" text changed!")
            sign = '@#-'
            try:
                nome = self.ORA.split(sign)[1].split('.')[0]
                self.setToolTip(nome)
            except:
                print('nome file non processato correttamente: ',self.ORA)
                print('riprovo')
                try:
                    nome = self.ORA.split('/')[-1].split('.')[0]
                    self.setToolTip(nome)
                except:
                    import traceback
                    print('niente da fare',traceback.format_exc())

            # print(" text changed: ", ora)
            return self.ORA, self.PRIMA
        else:
            print('no change')
            return


    def mouseMoveEvent(self, event):

        drag = QtGui.QDrag(self)
        dragMimeData = QtCore.QMimeData()
        dragMimeData.setText(self.text())
        drag.setMimeData(dragMimeData)
        self.setText('')
        self.ORA = ''
        drag.exec_(QtCore.Qt.MoveAction)


    def dragEnterEvent(self, event):
        # print("+++",self.text())
        # print("ob name: for {}".format(self.objectName()))
        # if self.text() == '':
        #     print("text is None for {}".format(self.objectName()))
        if event.mimeData().hasText():


            event.accept()

    def dropEvent(self, event):
        event.setDropAction(QtCore.Qt.MoveAction)
        # self.lbl.move(event.pos())  #moves label to position once the movement finishes (dropped)
        # print(event.mimeData().text())

        nome = event.mimeData().text().strip('[')
        nome = nome.strip(']')

        self.setText(nome)
        #todo commentare quella di sotto per rendere trasparente il nome del file
        # self.setStyleSheet('color:rgba(250,30,0,0)')
        self.setStyleSheet('color:rgba(250,30,0,250)')
        event.accept()


    def setText(self, p_str):
        # self.DROPPED.emit(self)
        self.TXT_CHANGED.emit(p_str)
        super(DroppableLabel, self).setText(p_str)
        # super(QtWidgets.QLabel, self).setText(p_str)

    # @QtCore.pyqtSlot(str)
    # def prova(self,w):
    #     print("prova ",w)
    #     # print("prova ",w.objectName())



class Test(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        myQWidget = QtWidgets.QWidget()
        myBoxLayout = QtWidgets.QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidgetA = MyListWidget(self)
        self.lab = DroppableLabel(self)
        # self.lab = LabelDrag()
        self.lab.setText("ciao")
        # self.lab.setMinimumHeight(64)
        # self.lab.setAcceptDrops(True)

        for i in range(5):
            listItemAInstance = MyListWidgetItem(str(i), i, parent=self.listWidgetA)

        myBoxLayout.addWidget(self.listWidgetA)
        myBoxLayout.addWidget(self.lab)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog_1 = Test()
    dialog_1.show()
    dialog_1.resize(480, 320)
    sys.exit(app.exec_())