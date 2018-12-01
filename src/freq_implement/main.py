# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/prinshu/SN/version_1/freq_implement/main.ui'
#
# Created: Wed Nov 28 22:02:15 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 265)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.topic = QtGui.QLineEdit(self.centralwidget)
        self.topic.setInputMask("")
        self.topic.setObjectName("topic")
        self.horizontalLayout.addWidget(self.topic)
        self.level = QtGui.QComboBox(self.centralwidget)
        self.level.setObjectName("level")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.horizontalLayout.addWidget(self.level)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.search = QtGui.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(0, QtGui.QApplication.translate("MainWindow", "class 10", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(1, QtGui.QApplication.translate("MainWindow", "class 9", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(2, QtGui.QApplication.translate("MainWindow", "class 8", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(3, QtGui.QApplication.translate("MainWindow", "class 7", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(4, QtGui.QApplication.translate("MainWindow", "class 6", None, QtGui.QApplication.UnicodeUTF8))
        self.level.setItemText(5, QtGui.QApplication.translate("MainWindow", "class 5", None, QtGui.QApplication.UnicodeUTF8))
        self.search.setText(QtGui.QApplication.translate("MainWindow", "Make Video", None, QtGui.QApplication.UnicodeUTF8))

