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
    def __init__(self, type, parent=None):
        super(MyListWidget, self).__init__(parent)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(False)
        self.viewport().setAcceptDrops(False)
        self.setDropIndicatorShown(True)

    def startDrag(self, supportedActions):
        drag = QtGui.QDrag(self)
        t = [i.GetData() for i in self.selectedItems()]
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


class DraggableLabel(QtWidgets.QLabel):
    def __init__(self, txt, parent):
        super(DraggableLabel, self).__init__(txt, parent)
        # QtWidgets.QLabel.__init__(self, txt, parent)
        self.setStyleSheet("QLabel { background-color: rgb(255, 255, 0)}")

    def mouseMoveEvent(self, event):
        drag = QtGui.QDrag(self)
        dragMimeData = QtCore.QMimeData()
        drag.setMimeData(dragMimeData)
        drag.exec_(QtCore.Qt.CopyAction)
        self.setText('')
    # def setText(self,text=str):
    #     self.setText(text)
    #     return


class LabelDrag(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.lbl = DraggableLabel("Drag me", self)
        self.lbl.setText("ciao")
        self.setAcceptDrops(True)
        self.setGeometry(40, 50, 200, 200)
        self.setMinimumHeight(64)
        self.show()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.setDropAction(QtCore.Qt.CopyAction)
        # self.lbl.move(event.pos())  #moves label to position once the movement finishes (dropped)
        # print(event.mimeData().text())

        nome = event.mimeData().text().strip('[')
        nome = nome.strip(']')
        # print("nome: ",nome)
        self.lbl.setText(nome)
        event.accept()


class Test(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        myQWidget = QtWidgets.QWidget()
        myBoxLayout = QtWidgets.QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidgetA = MyListWidget(self)
        self.lab = LabelDrag()
        # self.lab.setText("ciao")
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