from main import *
import sys
import os
import collections
from nltk import tokenize
from wiki_data import *
from text_to_video import *
from wiki_parser import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import codecs


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
			no_sentences = 20
			fpp = codecs.open("output_dictionary","r","utf-8")
			dictionary = {}
			for lines in fpp:
				words = [x.strip() for x in lines.split(' ')]
				dictionary[words[0]] = int(words[1])
			output_data = self.get_sentences_tdIdf(article,dictionary,no_sentences)	#Returns the top sentences from the article of the given number of sentences.
			fp = codecs.open("output.txt","w+","utf-8")
			for lines in output_data:
				fp.write(lines + "\n")
			pathFile = get_video()					#Converts the given file to video.      
			command = "vlc video.avi"
			os.system(command) 	
			
			
	def get_sentences_tdIdf(self,article_text,dictionary,no_sentences):
		'''article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
		article_text = re.sub(r'\s+', ' ', article_text) 
		formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
		article = re.sub(r'\s+', ' ', formatted_article_text)
		print article'''
		article = article_text
		sentences = sent_tokenize(article)
		n = len(sentences)
		score = []
		current = 0
		for lines in sentences:
			words = word_tokenize(lines)
			line_length = len(words)
			if line_length < 10:
				continue
			weight = 0
			for word in words :
				if word in dictionary:
					weight = weight + dictionary[word]
			if line_length == 0:
				score.append(0)
			else:
				score.append(float(weight)/float(line_length))
			current+=1
		selected = []
		selected_id = []
		final = {}
		for i in range(no_sentences):
			maxim = float(0)
			id_sentence = 0
			for j in range(current):
				if j in selected_id:
					continue
				elif maxim < score[j]:
					maxim = score[j]
					id_sentence = j
			selected.append(sentences[id_sentence])
			selected_id.append(id_sentence)
			final[id_sentence] = sentences[id_sentence]
			maxim = 0
			keylist = final.keys()
			keylist.sort()
			output = []
			for key in keylist:
				output.append(final[key])
		return output			
			
					
application()
