#!/usr/bin/python
# open file
import xlrd
import re
import nltk
from nltk.stem import WordNetLemmatizer as wnl

def preProcessData(tweet):
		
	
	#Remove HashTags
	tweet=re.sub('#','',tweet)
		
	#Remove Username like @Rahul
	tweet=re.sub('@[\w\d_]*','',tweet)

	#Remove URL's
	tweet=re.sub('http.//[\w\d\.\\/]*','',tweet)

	#Remove Puntuations
	tweet=re.sub(r'[%\.\'\"\?:,;!-]',' ',tweet)
	
	#Remove HTML Tags
	tweet=re.sub('<.*?>','',tweet)
		
	#Remove rpeadted Words
	tweet=re.sub(r'([a-z])\1+',r'\1',tweet)
		
	#Removing words that start with a number or a special character
	tweet = re.sub(r'^[^a-zA-Z]+',' ',tweet)
		
	#Convert camel Casing into space Separated word
	tweet=re.sub("([a-z])([A-Z])","\g<1> \g<2>",tweet)
		
	#Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
		
	#Remove StopWords
	tweet=tweet.split()
	nltkVariable=nltk.corpus.stopwords.words('english')
	for word in tweet:
		if word in nltkVariable:
			tweet.remove(word)
			
	#Lemmatize Words
	tweet=[wnl().lemmatize(word) for word in tweet]
		
	return tweet
		
	#preProcessData()		
