# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1227, 898)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1231, 901))
        self.label.setPixmap(QPixmap(u":/Image/Static/1381227.webp"))
        self.label.setScaledContents(True)
        self.image_show = QLabel(self.centralwidget)
        self.image_show.setObjectName(u"image_show")
        self.image_show.setGeometry(QRect(40, 110, 531, 571))
        self.image_show.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.image_show.setPixmap(QPixmap(u":/Image/Static/t\u00e9l\u00e9chargement.png"))
        self.image_show.setScaledContents(True)
        self.text_show = QLabel(self.centralwidget)
        self.text_show.setObjectName(u"text_show")
        self.text_show.setGeometry(QRect(650, 90, 531, 281))
        self.text_show.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.text_show.setPixmap(QPixmap(u":/Image/Static/images.png"))
        self.text_show.setScaledContents(True)
        self.select_btn = QPushButton(self.centralwidget)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(200, 700, 211, 51))
        self.pdf_btn = QPushButton(self.centralwidget)
        self.pdf_btn.setObjectName(u"pdf_btn")
        self.pdf_btn.setGeometry(QRect(840, 530, 181, 51))
        self.police_btn = QPushButton(self.centralwidget)
        self.police_btn.setObjectName(u"police_btn")
        self.police_btn.setGeometry(QRect(840, 440, 191, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.image_show.setText("")
        self.text_show.setText("")
        self.select_btn.setText(QCoreApplication.translate("MainWindow", u"S\u00e9lectionner", None))
        self.pdf_btn.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.police_btn.setText(QCoreApplication.translate("MainWindow", u"Prendre la police", None))
    # retranslateUi

