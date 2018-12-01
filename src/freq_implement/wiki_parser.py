import bs4 as bs  
import urllib 
import re
import codecs
def get_article(title):
	print title
	scraped_data = urllib.urlopen('https://en.wikipedia.org/wiki/'+title)  
	article = scraped_data.read()

	parsed_article = bs.BeautifulSoup(article,'lxml')

	paragraphs = parsed_article.find_all('p')

	article_text = ""

	for p in paragraphs:  
		article_text += p.text
		
	fp = codecs.open("article.txt","w+","utf-8")
	fp.write(article_text)
	return article_text
