# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VB_Gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1094, 640))
        MainWindow.setStyleSheet("#frame_svg{background-repeat: no-repeat;\n"
"border-image: url(:/immagine/_vb_interface_2.svg);\n"
" background-position: center;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(195, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.frame_svg_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_svg_2.sizePolicy().hasHeightForWidth())
        self.frame_svg_2.setSizePolicy(sizePolicy)
        self.frame_svg_2.setMinimumSize(QtCore.QSize(600, 400))
        self.frame_svg_2.setMaximumSize(QtCore.QSize(400, 400))
        self.frame_svg_2.setAcceptDrops(True)
        self.frame_svg_2.setStyleSheet("QLabel{\n"
"    background-color: rgba(117, 0, 75,0);}")
        self.frame_svg_2.setObjectName("frame_svg_2")
        self.label_slot_5 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_5.setGeometry(QtCore.QRect(389, 153, 101, 91))
        self.label_slot_5.setAcceptDrops(True)
        self.label_slot_5.setText("")
        self.label_slot_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_5.setObjectName("label_slot_5")
        self.label_slot_1 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_1.setGeometry(QtCore.QRect(80, 40, 101, 91))
        self.label_slot_1.setAcceptDrops(True)
        self.label_slot_1.setText("")
        self.label_slot_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_1.setObjectName("label_slot_1")
        self.label_slot_2 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_2.setGeometry(QtCore.QRect(250, 40, 101, 91))
        self.label_slot_2.setAcceptDrops(True)
        self.label_slot_2.setText("")
        self.label_slot_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_2.setObjectName("label_slot_2")
        self.label_slot_3 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_3.setGeometry(QtCore.QRect(426, 40, 101, 91))
        self.label_slot_3.setAcceptDrops(True)
        self.label_slot_3.setText("")
        self.label_slot_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_3.setObjectName("label_slot_3")
        self.label_slot_8 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_8.setGeometry(QtCore.QRect(424, 267, 101, 91))
        self.label_slot_8.setAcceptDrops(True)
        self.label_slot_8.setText("")
        self.label_slot_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_8.setObjectName("label_slot_8")
        self.label_slot_7 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_7.setGeometry(QtCore.QRect(252, 268, 101, 91))
        self.label_slot_7.setAcceptDrops(True)
        self.label_slot_7.setText("")
        self.label_slot_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_7.setObjectName("label_slot_7")
        self.label_slot_6 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_6.setGeometry(QtCore.QRect(80, 267, 101, 91))
        self.label_slot_6.setAcceptDrops(True)
        self.label_slot_6.setText("")
        self.label_slot_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_6.setObjectName("label_slot_6")
        self.label_slot_4 = QtWidgets.QLabel(self.frame_svg_2)
        self.label_slot_4.setGeometry(QtCore.QRect(115, 152, 101, 91))
        self.label_slot_4.setAcceptDrops(True)
        self.label_slot_4.setText("")
        self.label_slot_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_4.setObjectName("label_slot_4")
        self.frame_svg = QtWidgets.QFrame(self.frame_svg_2)
        self.frame_svg.setGeometry(QtCore.QRect(0, 0, 600, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_svg.sizePolicy().hasHeightForWidth())
        self.frame_svg.setSizePolicy(sizePolicy)
        self.frame_svg.setMinimumSize(QtCore.QSize(600, 400))
        self.frame_svg.setMaximumSize(QtCore.QSize(400, 400))
        self.frame_svg.setAcceptDrops(True)
        self.frame_svg.setStyleSheet("")
        self.frame_svg.setObjectName("frame_svg")
        self.frame_svg_3 = QtWidgets.QFrame(self.frame_svg)
        self.frame_svg_3.setGeometry(QtCore.QRect(0, 0, 600, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_svg_3.sizePolicy().hasHeightForWidth())
        self.frame_svg_3.setSizePolicy(sizePolicy)
        self.frame_svg_3.setMinimumSize(QtCore.QSize(600, 400))
        self.frame_svg_3.setMaximumSize(QtCore.QSize(400, 400))
        self.frame_svg_3.setAcceptDrops(True)
        self.frame_svg_3.setStyleSheet("QLabel{\n"
"    background-color: rgba(117, 255, 75,0);}")
        self.frame_svg_3.setObjectName("frame_svg_3")
        self.label_slot_5_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_5_dr.setGeometry(QtCore.QRect(389, 153, 101, 91))
        self.label_slot_5_dr.setAcceptDrops(True)
        self.label_slot_5_dr.setText("")
        self.label_slot_5_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_5_dr.setObjectName("label_slot_5_dr")
        self.label_slot_1_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_1_dr.setGeometry(QtCore.QRect(80, 40, 101, 91))
        self.label_slot_1_dr.setAcceptDrops(True)
        self.label_slot_1_dr.setText("")
        self.label_slot_1_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_1_dr.setObjectName("label_slot_1_dr")
        self.label_slot_2_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_2_dr.setGeometry(QtCore.QRect(250, 40, 101, 91))
        self.label_slot_2_dr.setAcceptDrops(True)
        self.label_slot_2_dr.setText("")
        self.label_slot_2_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_2_dr.setObjectName("label_slot_2_dr")
        self.label_slot_3_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_3_dr.setGeometry(QtCore.QRect(426, 40, 101, 91))
        self.label_slot_3_dr.setAcceptDrops(True)
        self.label_slot_3_dr.setText("")
        self.label_slot_3_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_3_dr.setObjectName("label_slot_3_dr")
        self.label_slot_8_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_8_dr.setGeometry(QtCore.QRect(424, 267, 101, 91))
        self.label_slot_8_dr.setAcceptDrops(True)
        self.label_slot_8_dr.setText("")
        self.label_slot_8_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_8_dr.setObjectName("label_slot_8_dr")
        self.label_slot_7_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_7_dr.setGeometry(QtCore.QRect(252, 268, 101, 91))
        self.label_slot_7_dr.setAcceptDrops(True)
        self.label_slot_7_dr.setText("")
        self.label_slot_7_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_7_dr.setObjectName("label_slot_7_dr")
        self.label_slot_6_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_6_dr.setGeometry(QtCore.QRect(80, 267, 101, 91))
        self.label_slot_6_dr.setAcceptDrops(True)
        self.label_slot_6_dr.setText("")
        self.label_slot_6_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_6_dr.setObjectName("label_slot_6_dr")
        self.label_slot_4_dr = QtWidgets.QLabel(self.frame_svg_3)
        self.label_slot_4_dr.setGeometry(QtCore.QRect(115, 152, 101, 91))
        self.label_slot_4_dr.setAcceptDrops(True)
        self.label_slot_4_dr.setText("")
        self.label_slot_4_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot_4_dr.setObjectName("label_slot_4_dr")
        self.gridLayout.addWidget(self.frame_svg_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(195, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_strumenti = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_strumenti.sizePolicy().hasHeightForWidth())
        self.comboBox_strumenti.setSizePolicy(sizePolicy)
        self.comboBox_strumenti.setObjectName("comboBox_strumenti")
        self.verticalLayout_3.addWidget(self.comboBox_strumenti)
        self.lista_suoni = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lista_suoni.sizePolicy().hasHeightForWidth())
        self.lista_suoni.setSizePolicy(sizePolicy)
        self.lista_suoni.setMinimumSize(QtCore.QSize(191, 452))
        self.lista_suoni.setMaximumSize(QtCore.QSize(191, 452))
        self.lista_suoni.setObjectName("lista_suoni")
        self.verticalLayout_3.addWidget(self.lista_suoni)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bot_rimuovi = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_rimuovi.sizePolicy().hasHeightForWidth())
        self.bot_rimuovi.setSizePolicy(sizePolicy)
        self.bot_rimuovi.setObjectName("bot_rimuovi")
        self.horizontalLayout_5.addWidget(self.bot_rimuovi)
        self.bot_rimuovi_cat = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_rimuovi_cat.sizePolicy().hasHeightForWidth())
        self.bot_rimuovi_cat.setSizePolicy(sizePolicy)
        self.bot_rimuovi_cat.setObjectName("bot_rimuovi_cat")
        self.horizontalLayout_5.addWidget(self.bot_rimuovi_cat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bot_aggiungi = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_aggiungi.sizePolicy().hasHeightForWidth())
        self.bot_aggiungi.setSizePolicy(sizePolicy)
        self.bot_aggiungi.setObjectName("bot_aggiungi")
        self.horizontalLayout_3.addWidget(self.bot_aggiungi)
        self.bot_nuovaCartella = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_nuovaCartella.sizePolicy().hasHeightForWidth())
        self.bot_nuovaCartella.setSizePolicy(sizePolicy)
        self.bot_nuovaCartella.setObjectName("bot_nuovaCartella")
        self.horizontalLayout_3.addWidget(self.bot_nuovaCartella)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bot_esci = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_esci.sizePolicy().hasHeightForWidth())
        self.bot_esci.setSizePolicy(sizePolicy)
        self.bot_esci.setObjectName("bot_esci")
        self.horizontalLayout.addWidget(self.bot_esci)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bot_connetti = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_connetti.sizePolicy().hasHeightForWidth())
        self.bot_connetti.setSizePolicy(sizePolicy)
        self.bot_connetti.setObjectName("bot_connetti")
        self.horizontalLayout.addWidget(self.bot_connetti)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.radio_hotSpot = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_hotSpot.setChecked(True)
        self.radio_hotSpot.setObjectName("radio_hotSpot")
        self.horizontalLayout_4.addWidget(self.radio_hotSpot)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.spinner = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinner.sizePolicy().hasHeightForWidth())
        self.spinner.setSizePolicy(sizePolicy)
        self.spinner.setMinimumSize(QtCore.QSize(60, 60))
        self.spinner.setMaximumSize(QtCore.QSize(60, 60))
        self.spinner.setObjectName("spinner")
        self.horizontalLayout_4.addWidget(self.spinner)
        self.bot_applica = QtWidgets.QPushButton(self.centralwidget)
        self.bot_applica.setObjectName("bot_applica")
        self.horizontalLayout_4.addWidget(self.bot_applica)
        self.bot_salva_preset = QtWidgets.QPushButton(self.centralwidget)
        self.bot_salva_preset.setObjectName("bot_salva_preset")
        self.horizontalLayout_4.addWidget(self.bot_salva_preset)
        self.bot_carica_preset = QtWidgets.QPushButton(self.centralwidget)
        self.bot_carica_preset.setObjectName("bot_carica_preset")
        self.horizontalLayout_4.addWidget(self.bot_carica_preset)
        self.bot_pulisci = QtWidgets.QPushButton(self.centralwidget)
        self.bot_pulisci.setObjectName("bot_pulisci")
        self.horizontalLayout_4.addWidget(self.bot_pulisci)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bot_impostazioni = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_impostazioni.sizePolicy().hasHeightForWidth())
        self.bot_impostazioni.setSizePolicy(sizePolicy)
        self.bot_impostazioni.setObjectName("bot_impostazioni")
        self.horizontalLayout_2.addWidget(self.bot_impostazioni)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VB Interface"))
        self.bot_rimuovi.setText(_translate("MainWindow", "rimuovi"))
        self.bot_rimuovi_cat.setText(_translate("MainWindow", "categoria -"))
        self.bot_aggiungi.setText(_translate("MainWindow", "file +"))
        self.bot_nuovaCartella.setText(_translate("MainWindow", "categoria +"))
        self.bot_esci.setText(_translate("MainWindow", "esci"))
        self.bot_connetti.setText(_translate("MainWindow", "Connetti"))
        self.radio_hotSpot.setText(_translate("MainWindow", "Hot Spot"))
        self.bot_applica.setText(_translate("MainWindow", "applica"))
        self.bot_salva_preset.setText(_translate("MainWindow", "salva preset"))
        self.bot_carica_preset.setText(_translate("MainWindow", "carica preset"))
        self.bot_pulisci.setText(_translate("MainWindow", "pulisci"))
        self.bot_impostazioni.setText(_translate("MainWindow", "impostazioni"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


import vegeboard_svg_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())