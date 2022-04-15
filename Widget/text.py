# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/text.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1231, 901))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Image/Static/1381227.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.image_show = QtWidgets.QLabel(self.centralwidget)
        self.image_show.setGeometry(QtCore.QRect(40, 110, 531, 571))
        self.image_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.image_show.setText("")
        self.image_show.setPixmap(QtGui.QPixmap(":/Image/Static/téléchargement.png"))
        self.image_show.setScaledContents(True)
        self.image_show.setObjectName("image_show")
        self.text_show = QtWidgets.QLabel(self.centralwidget)
        self.text_show.setGeometry(QtCore.QRect(660, 100, 531, 281))
        self.text_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_show.setText("")
        self.text_show.setPixmap(QtGui.QPixmap(":/Image/Static/images.png"))
        self.text_show.setScaledContents(True)
        self.text_show.setObjectName("text_show")
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setGeometry(QtCore.QRect(200, 700, 211, 51))
        self.select_btn.setObjectName("select_btn")
        self.pdf_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pdf_btn.setGeometry(QtCore.QRect(840, 530, 181, 51))
        self.pdf_btn.setObjectName("pdf_btn")
        self.police_btn = QtWidgets.QPushButton(self.centralwidget)
        self.police_btn.setGeometry(QtCore.QRect(840, 440, 191, 51))
        self.police_btn.setObjectName("police_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_btn.setText(_translate("MainWindow", "Sélectionner"))
        self.pdf_btn.setText(_translate("MainWindow", "PDF"))
        self.police_btn.setText(_translate("MainWindow", "Prendre la police"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
