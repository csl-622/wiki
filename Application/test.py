from main import *
import sys

class application(QtGui.QMainWindow):
	def __init__(self):
		self.app = QtGui.QApplication(sys.argv)
		self.app.setWindowIcon(QtGui.QIcon('ico.png'))
		self.Dialog = QtGui.QMainWindow()
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
        	self.showMaximized()
        	self.ui.search.clicked.connect(lambda: self.findArticle(self.ui.topic.text()))
        	r = self.app.exec_()
        	sys.exit(r)
        	
	def findArticle(self,topic):
		if len(topic) == 0:
			msgBox = QtGui.QMessageBox()
        		msgBox.setText("Please enter a valid topic.")
        		msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        		msgBox.setDefaultButton(QtGui.QMessageBox.Ok)
        		ret = msgBox.exec_()
		else:
			print topic       	
application()
