#!/usr/bin/python
# open file
import xlrd
import re
import nltk
from nltk.stem import WordNetLemmatizer as wnl

wb=xlrd.open_workbook('Tweets.xls')
Obamash=wb.sheet_by_index(0);
#Obamatweets=Obamash.col_values(4)

Romneysh=wb.sheet_by_index(1);
#Romneytweets=Romneysh.col_values(4)

#f = open ("C:\Users\Rahul\Desktop\q.txt","r")
obamaTuple= []
obamaTweet=[]
for rownum in range(Obamash.nrows):
	obamaTuple=(unicode((Obamash.cell(rownum,3).value)).encode('utf-8'),(Obamash.cell(rownum,6).value))
	obamaTweet.append(obamaTuple)
	
RomneyTuple=[]
RomneyTweet=[]
for rownum in range(Romneysh.nrows):
	RomneyTuple=((Romneysh.cell(rownum,3).value),(Romneysh.cell(rownum,6).value))
	RomneyTweet.append(RomneyTuple)

#Removes Punctutaions
def checkPuntuations(obamaTweet):
	count=0
	while count < len(obamaTweet):
		#tweet=(unicode(obamaTweet[count])).encode('utf-8')
		#tweet=str(tweet)
		tweet=obamaTweet[count]
		obamaTweet[count]=re.sub(r'[%\.\'\"\?:,;!-]',' ',tweet)
		count=count+1

#Removes URLs of the form https://charecters		
def checkURL(obamaTweet):
	count=0
	while count < len(obamaTweet):
		tweet=(unicode(obamaTweet[count])).encode('utf-8')
		tweet=str(tweet)
		obamaTweet[count]=re.sub('http.//[\w\d\.\\/]*','',tweet)
		count=count+1

#Removes the username of the form @Rahul
def checkUsername(obamaTweet):
	count=0
	while count < len(obamaTweet):
		#tweet=(unicode(obamaTweet[count])).encode('utf-8')
		#tweet=str(tweet)
		tweet=obamaTweet[count]
		obamaTweet[count]=re.sub('@[\w\d_]*','',tweet)
		count=count+1

#Removes the hashTags		
def checkHashTag(obamaTweet):
	count=0
	while count < len(obamaTweet):
		#tweet=(unicode(obamaTweet[count])).encode('utf-8')
		#tweet=str(tweet)
		tweet=obamaTweet[count]
		obamaTweet[count]=re.sub('#','',tweet)
		count=count+1	
		
#Removes HTML tags of the form <*>		
def checkHtmlTag(obamaTweet):
	count=0
	while count < len(obamaTweet):
		#tweet=(unicode(obamaTweet[count])).encode('utf-8')
		#tweet=str(tweet)
		tweet=obamaTweet[count]
		obamaTweet[count]=re.sub('<.*?>','',tweet)
		count=count+1		
		
#Removes Stop Words		
def checkStopWords(obamaTweet):
	count=0
	while count < len(obamaTweet):
		#tweet=(unicode(obamaTweet[count])).encode('utf-8')
		#tweet=str(tweet)
		tweet=obamaTweet[count]
		tweet=tweet.split()
		nltkVariable=nltk.corpus.stopwords.words('english')
		for word in tweet:
			if word in nltkVariable:
				tweet.remove(word)
		obamaTweet[count]=tweet
		count=count+1
		
def checkRepeatedWord(obamaTweet):
	count=0
	while count < len(obamaTweet):
		#tweet=(unicode(obamaTweet[count])).encode('utf-8')
		#tweet=str(tweet)
		tweet=obamaTweet[count]
		obamaTweet[count]=re.sub(r'([a-z])\1+',r'\1',tweet)
		count=count+1	

def preProcessData(tuple):
	count=0
	for tweet,sentiment in tuple:	
	
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
		
		if count==6:
			#print tweet
		#	tweet=re.sub('http.//[\w\d\.\\/]*','',tweet)
			print tweet
		count=count+1
		
preProcessData(obamaTweet)		
#print (obamaTweet[6])
#checkURL(obamaTweet)
#checkPuntuations(obamaTweet)
#checkUsername(obamaTweet)
#checkHashTag(obamaTweet)
#checkHtmlTag(obamaTweet)
#checkRepeatedWord(obamaTweet)
#checkStopWords(obamaTweet)

#print (obamaTweet[6])
	


#Read whole file into data
#data = f.read()
# Print it
#print data
# Close the file
#f.close()