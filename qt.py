# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledbYLMsN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1029, 676)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(11, 15, 71);\n"
"border-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setEnabled(True)
        self.line.setGeometry(QRect(310, 0, 16, 681))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"selection-color: rgb(255, 255, 255);")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.horizontalSlider = QSlider(self.frame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(70, 250, 160, 22))
        self.horizontalSlider.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.horizontalSlider.setMaximum(360)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2 = QSlider(self.frame)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(70, 320, 160, 22))
        self.horizontalSlider_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalSlider_2.setMaximum(360)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(400, 150, 561, 451))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0,0,0,0);\n"
"border-radius:10px;\n"
"border: 2px solid #ffffff\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 201, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"border: none\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 60, 501, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.frame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(240, 250, 64, 23))
        self.lcdNumber_2 = QLCDNumber(self.frame)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(240, 320, 64, 23))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 70, 401, 16))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 60, 221, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 120, 113, 22))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 180, 113, 22))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 120, 31, 16))
        self.label_5.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 180, 31, 16))
        self.label_6.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 250, 41, 21))
        self.label_7.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 310, 61, 31))
        self.label_8.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 370, 93, 28))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(380, 630, 561, 20))
        self.label_9.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(880, 20, 141, 111))
        self.label_10.setStyleSheet(u"image: url(:/log/unt_logo.png);")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(350, 30, 111, 91))
        self.label_11.setStyleSheet(u"image: url(:/log/Pasted-2023921-192d303.png);")

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Curva de Acoplador", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"UNIVERSIDAD NACIONAL DE TRUJILLO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Parametros de entrada", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"L2:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"r:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"alfa", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ganma", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SIMULAR", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dise\u00f1ado por Brayan Stalin Vera Noriega y William Jes\u00fas Salazar Llamoga", None))
        self.label_10.setText("")
        self.label_11.setText("")
    # retranslateUi

