# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/prinshu/SN/main.ui'
#
# Created: Sun Nov  4 01:42:33 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search = QtGui.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(350, 310, 101, 29))
        self.search.setObjectName("search")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 230, 531, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.topic = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.topic.setInputMask("")
        self.topic.setObjectName("topic")
        self.horizontalLayout.addWidget(self.topic)
        self.level = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.level.setObjectName("level")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.horizontalLayout.addWidget(self.level)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.search.setText(QtGui.QApplication.translate("MainWindow", "Make Video", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(0, QtGui.QApplication.translate("MainWindow", "class 10", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(1, QtGui.QApplication.translate("MainWindow", "class 9", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(2, QtGui.QApplication.translate("MainWindow", "class 8", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(3, QtGui.QApplication.translate("MainWindow", "class 7", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(4, QtGui.QApplication.translate("MainWindow", "class 6", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(5, QtGui.QApplication.translate("MainWindow", "class 5", None, QtGui.QApplication.UnicodeUTF8))
