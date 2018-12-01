from main import *
import sys
import os
import collections
import nltk
from wiki_data import *
from text_to_video import *
from wiki_parser import *
import re
import heapq  

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
			
			path = os.getcwd()
			#pathFile = get_wiki_byname([topic])				#Downloads the given articles xml file
			article = get_article(topic)									#returns a list of sentences in the xml file.
			no_sentences = 10
			pathFile = "python3 " + path + "/freq.py"	#Returns the top sentences from the article of the given number of sentences.
			os.system(pathFile)
			pathFile = get_video()					#Converts the given file to video.
			print topic  
			command = "vlc video.avi"
			os.system(command) 	
			

application()
