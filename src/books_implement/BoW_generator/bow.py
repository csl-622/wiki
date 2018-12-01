import os
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs

def make_dictionary(fileName):
	fp = codecs.open(fileName,"r","utf-8")
	dictionary = {}
	for lines in fp:
		words = word_tokenize(lines)
		for word in words:
			if word in dictionary:
				dictionary[word] = dictionary[word]+1
			else:
				dictionary[word] = 1
	return dictionary
			
	
def find_common(d_list,threshold):
	num = 0
	common_words = []
	total_dict = len(d_list)
	for dictionary in d_list:
		for word,times in dictionary.items():
			if word in common_words:
				continue
			count = 0
			dict_no = 0
			for diction in d_list:
				if dict_no==num:
					dict_no+=1
					continue
				else:
					if word in diction:
						if diction[word] > threshold:
							count+=1
				dict_no+=1
			if count == total_dict-1:
				common_words.append(word)
				
		num+=1
		
	return common_words
	
def remove_common(d_list,common_words):
	for words in common_words:
		for dictionary in d_list:
			if words in dictionary:
				del dictionary[words]
	return d_list
	
def make_dictionary_nltp(fileName,dictionary):
	fp = codecs.open(fileName,"r","utf-8")
	stop_words = set(stopwords.words('english'))
	for lines in fp:
		words = word_tokenize(lines)
		for word in words:
			if word not in stop_words:
				if word in dictionary:
					dictionary[word] = dictionary[word]+1
				else:
					dictionary[word] = 1
	return dictionary
	
	
def tdIdf(d_list):
	final_dict = {}
	num = 0
	no_dict = len(d_list)
	for dictionary in d_list:
		for word,freq in dictionary.items():
			if word in final_dict:
				continue
			count = 0
			dict_no = 0
			score = 0
			for diction in d_list:
				if dict_no==num:
					dict_no+=1
					continue
				else:	
					if word in diction:
						count+=1
			score = freq*math.log10(no_dict/count)
			final_dict[word] = score
			dict_no+=1
		num+=1
	return final_dict
	
def write_to_file(dictionary):
	fp = codecs.open("../output_dictionary","w+","utf-8")
	for word,freq in dictionary.items():
		fp.write(word + " " + str(freq) + "\n")

def make_dictionary_list(path,threshold):
	fileList = [files for files in os.listdir(path) if files.endswith(".txt")]
	file_no = len(fileList)
	dicts = []
	dictionary_nltp = {}
	for files in fileList:	
		dict1 = make_dictionary(path + "/" + files)
		dictionary_nltp = make_dictionary_nltp(path + "/" + files,dictionary_nltp)
		dicts.append(dict1)
	#common = find_common(dicts,threshold)
	#dicts = remove_common(dicts,common)
	for dict in dicts:
		write_to_file(dict)
	#return dicts
	write_to_file(dictionary_nltp)
	return dictionary_nltp
	
	
dictionary = make_dictionary_list("textFiles",0)
print ("Dictionary saved in parent folder.")
			
		
