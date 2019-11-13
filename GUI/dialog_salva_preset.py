# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_salva_preset.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_salva_preset(object):
    def setupUi(self, Dialog_salva_preset):
        Dialog_salva_preset.setObjectName("Dialog_salva_preset")
        Dialog_salva_preset.setWindowModality(QtCore.Qt.WindowModal)
        Dialog_salva_preset.resize(360, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_salva_preset.sizePolicy().hasHeightForWidth())
        Dialog_salva_preset.setSizePolicy(sizePolicy)
        Dialog_salva_preset.setMinimumSize(QtCore.QSize(360, 180))
        Dialog_salva_preset.setMaximumSize(QtCore.QSize(360, 180))
        Dialog_salva_preset.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_salva_preset)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog_salva_preset)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_salva_preset)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_salva_preset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonBox.setMaximumSize(QtCore.QSize(360, 215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(Dialog_salva_preset)
        self.buttonBox.accepted.connect(Dialog_salva_preset.accept)
        self.buttonBox.rejected.connect(Dialog_salva_preset.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_salva_preset)

    def retranslateUi(self, Dialog_salva_preset):
        _translate = QtCore.QCoreApplication.translate
        Dialog_salva_preset.setWindowTitle(_translate("Dialog_salva_preset", "Salva Preset"))
        self.label.setText(_translate("Dialog_salva_preset", "Nome:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_salva_preset = QtWidgets.QDialog()
    ui = Ui_Dialog_salva_preset()
    ui.setupUi(Dialog_salva_preset)
    Dialog_salva_preset.show()
    sys.exit(app.exec_())
