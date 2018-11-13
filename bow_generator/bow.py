import os

def make_dictionary(fileName):
	fp = open(fileName,"r")
	dictionary = {}
	for lines in fp:
		words = [x.strip() for x in lines.split(' ')]
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

def make_dictionary_list(path,threshold):
	fileList = [files for files in os.listdir(path) if files.endswith(".txt")]
	file_no = len(fileList)
	dicts = []
	for files in fileList:	
		dict1 = make_dictionary(path + "/" + files)
		dicts.append(dict1)
	common = find_common(dicts,threshold)
	dicts = remove_common(dicts,common)
	print "Dictionary length is : ",
	print len(dicts)
	return dicts
	
dictionary = make_dictionary_list("textFiles",0)
print dictionary
			
		
