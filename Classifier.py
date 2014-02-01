from ReadExcel import ReadExcel
from DataPreProcessing import preProcessData
import collections, itertools
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist


PosTweets=[]
NegTweets=[]
NeutralTweets=[]
MixedTweets=[]
obamaTweets=[]

def evaluate_classifier(featx):
	#print 'Rahul Sharma'
	
	posfeats = [(featx(tweets),'pos') for tweets, sent in PosTweets]
	negfeats = [(featx(tweets),'neg') for tweets, sent in NegTweets]
	neufeats = [(featx(tweets),'neu') for tweets, sent in NeutralTweets]
	mixgfeats = [(featx(tweets),'mix') for tweets, sent in MixedTweets]
	
	negcutoff = len(negfeats)*3/4
	poscutoff = len(posfeats)*3/4
	mixcutoff = len(mixgfeats)*3/4
	neucutoff = len(neufeats)*3/4

	trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff] + mixgfeats[:mixcutoff] + neufeats[:neucutoff] 
	testfeats = negfeats[negcutoff:] + posfeats[poscutoff:] + mixgfeats[mixcutoff:] + neufeats[neucutoff:]
	
	classifier = NaiveBayesClassifier.train(trainfeats)
	refsets = collections.defaultdict(set)
	testsets = collections.defaultdict(set)
	
	for i, (feats, label) in enumerate(testfeats):
		refsets[label].add(i)
		observed = classifier.classify(feats)
		testsets[observed].add(i)
	print '===================================================\n'
	print 'POSITIVE VALUES\n'	
	print '===================================================\n'
	print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
	print 'pos precision:', nltk.metrics.precision(refsets['pos'], testsets['pos'])
	print 'pos recall:', nltk.metrics.recall(refsets['pos'], testsets['pos'])
	print 'pos F-score:', nltk.metrics.f_measure(refsets['pos'], testsets['pos'])
	
	print '===================================================\n'
	print 'NEGETIVE VALUES\n'	
	print '===================================================\n'
	print 'neg precision:', nltk.metrics.precision(refsets['neg'], testsets['neg'])
	print 'neg recall:', nltk.metrics.recall(refsets['neg'], testsets['neg'])
	print 'neg F-score:', nltk.metrics.f_measure(refsets['neg'], testsets['neg'])
	
	print '===================================================\n'
	print 'MIXED VALUES\n'	
	print '===================================================\n'
	print 'mix precision:', nltk.metrics.precision(refsets['mix'], testsets['mix'])
	print 'mix recall:', nltk.metrics.recall(refsets['mix'], testsets['mix'])
	print 'mix F-score:', nltk.metrics.f_measure(refsets['mix'], testsets['mix'])
	
	print '===================================================\n'
	print 'NEUTRAL VALUES\n'	
	print '===================================================\n'
	print 'neu precision:', nltk.metrics.precision(refsets['neu'], testsets['neu'])
	print 'neu recall:', nltk.metrics.recall(refsets['neu'], testsets['neu'])
	print 'neu F-score:', nltk.metrics.f_measure(refsets['neu'], testsets['neu'])
	#classifier.show_most_informative_features()
	
def word_feats(words):
    return dict([(word, True) for word in words])
	
def separateTweets(Tweets):
	count=0
	for tweet,sentiment in Tweets:
		if sentiment==1.0:
			PosTweets.append((preProcessData(tweet),sentiment))
			#print 'Rahul'
		elif sentiment==-1.0:
			NegTweets.append((preProcessData(tweet),sentiment))
		elif sentiment==0.0:
			NeutralTweets.append((preProcessData(tweet),sentiment))
		elif sentiment==2.0:
			MixedTweets.append((preProcessData(tweet),sentiment))	
	
	
		
def ReadTweets():	
	obamaTweets,RomneyTweets=ReadExcel().readTweets()
	#RomneyTweets=ReadExcel().readRomneyTweets()
	print'***********************************OBAMA TWEETS***************************************'
	separateTweets(obamaTweets)
	print 'evaluating single word features for Obama'
	evaluate_classifier(word_feats)
	
	print'**********************************ROMNEY TWEETS***************************************'
	separateTweets(RomneyTweets)	
	print 'evaluating single word features for Romney'
	evaluate_classifier(word_feats)
ReadTweets()	

 

 
#print 'evaluating single word features'
#evaluate_classifier(word_feats)