# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\chengley\ups-relationship\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labell = QtWidgets.QLabel(self.centralwidget)
        self.labell.setObjectName("labell")
        self.gridLayout.addWidget(self.labell, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 2, 5, 2, 3)
        self.pushButtonr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonr.setObjectName("pushButtonr")
        self.gridLayout.addWidget(self.pushButtonr, 4, 6, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 3, 3, 1, 2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 3, 1, 2)
        self.pushButtons = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtons.setObjectName("pushButtons")
        self.gridLayout.addWidget(self.pushButtons, 4, 5, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 4, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.pushButtonl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonl.setObjectName("pushButtonl")
        self.gridLayout.addWidget(self.pushButtonl, 4, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.pushButtonshow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonshow.setObjectName("pushButtonshow")
        self.gridLayout.addWidget(self.pushButtonshow, 5, 6, 1, 1)
        self.pushButtonv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonv.setObjectName("pushButtonv")
        self.gridLayout.addWidget(self.pushButtonv, 4, 4, 1, 1)
        self.labelt = QtWidgets.QLabel(self.centralwidget)
        self.labelt.setText("")
        self.labelt.setObjectName("labelt")
        self.gridLayout.addWidget(self.labelt, 1, 4, 1, 1)
        self.labeld = QtWidgets.QLabel(self.centralwidget)
        self.labeld.setText("")
        self.labeld.setObjectName("labeld")
        self.gridLayout.addWidget(self.labeld, 5, 3, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labell.setText(_translate("MainWindow", "视频列表"))
        self.label.setText(_translate("MainWindow", "输入"))
        self.pushButtonr.setText(_translate("MainWindow", "读取json"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "少年Pi,api,A_Pi,少年PI,API"))
        self.pushButtons.setText(_translate("MainWindow", "保存json"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.06294pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9.06294pt;\">输入tag列表</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9.06294pt;\">example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9.06294pt; font-weight:600;\">少年Pi,api,A_Pi,少年PI,API</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.06294pt;\"><br /></p></body></html>"))
        self.pushButtonl.setText(_translate("MainWindow", "拉取视频列表"))
        self.label_4.setText(_translate("MainWindow", "拉取量"))
        self.pushButtonshow.setText(_translate("MainWindow", "展示数据表"))
        self.pushButtonv.setText(_translate("MainWindow", "获取视频数据"))
