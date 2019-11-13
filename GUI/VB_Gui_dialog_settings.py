# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VB_Gui_dialog_settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_impostazioni(object):
    def setupUi(self, Dialog_impostazioni):
        Dialog_impostazioni.setObjectName("Dialog_impostazioni")
        Dialog_impostazioni.resize(640, 480)
        Dialog_impostazioni.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_impostazioni)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 64, 128, 64)
        self.verticalLayout.setSpacing(60)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog_impostazioni)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_impostazioni)
        self.lineEdit.setMinimumSize(QtCore.QSize(201, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog_impostazioni)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_impostazioni)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(201, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog_impostazioni)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog_impostazioni)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(201, 20))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(201, 20))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.bot_settings_box = QtWidgets.QDialogButtonBox(Dialog_impostazioni)
        self.bot_settings_box.setOrientation(QtCore.Qt.Vertical)
        self.bot_settings_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bot_settings_box.setObjectName("bot_settings_box")
        self.gridLayout.addWidget(self.bot_settings_box, 0, 1, 1, 1)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_3.setBuddy(self.lineEdit_3)

        self.retranslateUi(Dialog_impostazioni)
        self.bot_settings_box.accepted.connect(Dialog_impostazioni.accept)
        self.bot_settings_box.rejected.connect(Dialog_impostazioni.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_impostazioni)

    def retranslateUi(self, Dialog_impostazioni):
        _translate = QtCore.QCoreApplication.translate
        Dialog_impostazioni.setWindowTitle(_translate("Dialog_impostazioni", "Settings"))
        self.label.setText(_translate("Dialog_impostazioni", "indirizzo:"))
        self.lineEdit.setText(_translate("Dialog_impostazioni", "192.168.4.1"))
        self.label_2.setText(_translate("Dialog_impostazioni", "rete:"))
        self.lineEdit_2.setText(_translate("Dialog_impostazioni", "Vodafone-newstarsys"))
        self.label_3.setText(_translate("Dialog_impostazioni", "password:"))
        self.lineEdit_3.setText(_translate("Dialog_impostazioni", "bavariaRose@0wifi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_impostazioni = QtWidgets.QDialog()
    ui = Ui_Dialog_impostazioni()
    ui.setupUi(Dialog_impostazioni)
    Dialog_impostazioni.show()
    sys.exit(app.exec_())

