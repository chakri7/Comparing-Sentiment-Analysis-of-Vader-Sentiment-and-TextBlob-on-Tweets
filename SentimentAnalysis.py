
import sys

import re

import tweepy

from tweepy import OAuthHandler

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt1

analyzer = SentimentIntensityAnalyzer()

class TwitterClient(object):

'''

Generic Twitter Class for sentiment analysis.



'''



def __init__(self):

'''

Class constructor or initialization method.

'''

#	keys and tokens from the Twitter Dev Console consumer_key = 'x9Rxt3YCwUbCTb2c4vmm4xKsU'






34
 
consumer_secret = '4IhQrSsHojfkEAQVGpWy76cu1bidQzg18Rb5ITkgi9vMJwvVQP'

access_token	=	'784965978-

XwNxRRRewXEcMFMbNOHPymiDxZhAjWFusyZnt5OT'

access_token_secret = 'sgQC8lJCrslcsnf2fBRS5dwlKSdpeuumMuBd3PWwHM6We'

#	attempt authentication try:

#	create OAuthHandler object

self.auth = OAuthHandler(consumer_key, consumer_secret)

# set access token and secret

self.auth.set_access_token(access_token, access_token_secret)

#	create tweepy API object to fetch tweets self.api = tweepy.API(self.auth)

except:

print("Error: Authentication Failed")

def clean_tweet(self, tweet):

'''

Utility function to clean tweet text by removing links, special characters

using simple regex statements.

'''

return tweet

def clean_tweet1(self, tweet):

'''

Utility function to clean tweet text by removing links, special characters using simple regex statements.



35
 
Removing Stowords

'''

stopword_set = set(stopwords.words("english"))

return " ".join([i for i in re.sub(r'[^a-zA-Z\s]', "", tweet).lower().split() if

i	not in stopword_set]) #return tweet

def get_tweet_sentiment(self, tweet): #implementing vader sentiment analyzer vs = analyzer.polarity_scores(tweet)

# set sentiment

if vs['compound'] > 0:

return 'positive'

elif vs['compound'] == 0:

return 'neutral'

else:

return 'negative'

def get_tweets(self, query, count = 10):

'''

Main function to fetch tweets and parse them.

'''

#	empty list to store parsed tweets tweets = []

try:




36
 
# call twitter api to fetch tweets

fetched_tweets = self.api.search(q = query, count = count)



#	parsing tweets one by one for tweet in fetched_tweets:

parsed_tweet = {}



# saving text of tweet

parsed_tweet['text'] = tweet.text

#	saving sentiment of tweet sre=TwitterClient.clean_tweet(self,tweet.text) #se=TwitterClient.clean_tweet1(self,tweet.text) parsed_tweet['sentiment'] = self.get_tweet_sentiment(sre)

#	appending parsed tweet to tweets list

if tweet.retweet_count > 0:

#	if tweet has retweets, ensure that it is appended only once if parsed_tweet not in tweets:

tweets.append(parsed_tweet)

else:

tweets.append(parsed_tweet)



#	return parsed tweets return tweets

except tweepy.TweepError as e:




37
 
#	print error (if any) print("Error : " + str(e))

def get_tweets1(self, query, count = 10):

'''

Main function to fetch tweets and parse them.

'''

#	empty list to store parsed tweets tweets1 = []

try:

# call twitter api to fetch tweets

fetched_tweets = self.api.search(q = query, count = count)



#	parsing tweets one by one for tweet in fetched_tweets:

#	empty dictionary to store required params of a tweet parsed_tweet = {}

#	saving text of tweet

parsed_tweet['text'] = tweet.text

#	saving sentiment of tweet #sre=TwitterClient.clean_tweet(self,tweet.text) se=TwitterClient.clean_tweet1(self,tweet.text) parsed_tweet['sentiment'] = self.get_tweet_sentiment(se)

#	appending parsed tweet to tweets list

if tweet.retweet_count > 0:




38
 
#	if tweet has retweets, ensure that it is appended only once if parsed_tweet not in tweets1:

tweets1.append(parsed_tweet)

else:

tweets1.append(parsed_tweet)



#	return parsed tweets return tweets1

except tweepy.TweepError as e:

#	print error (if any) print("Error : " + str(e))

def main():

#	creating object of TwitterClient Class api = TwitterClient()

#	calling function to get tweets

tweets = api.get_tweets(query = 'Narendra Modi', count = 10000)

tweets1 = api.get_tweets1(query = 'Narendra Modi', count = 10000)

tweets2 = api.get_tweets1(query = 'Rahul Gandhi', count = 10000)



# picking positive tweets from tweets

ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] ptweets1 = [tweet for tweet in tweets1 if tweet['sentiment'] == 'positive'] ptweets2 = [tweet for tweet in tweets2 if tweet['sentiment'] == 'positive'] # percentage of positive tweets





39
 
print("Positive	tweets	percentage:

{} %".format(100*len(ptweets)/len(tweets)))

print("Positive	tweets	after	pre-processing	percentage	Modi:

{} %".format(100*len(ptweets1)/len(tweets1)))

print("Positive tweets after pre-processing percentage Rahul Gandhi:

{} %".format(100*len(ptweets2)/len(tweets2)))

# picking negative tweets from tweets

ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] ntweets1 = [tweet for tweet in tweets1 if tweet['sentiment'] == 'negative'] ntweets2= [tweet for tweet in tweets2 if tweet['sentiment'] == 'negative'] # percentage of negative tweets

print("Negative	tweets	percentage:

{} %".format(100*len(ntweets)/len(tweets)))

print("Negative	tweets	after	pre-processing	percentage	Modi:

{} %".format(100*len(ntweets1)/len(tweets1)))

print("Negative	tweets	after	pre-processing	percentage	Rahul:

{} %".format(100*len(ntweets2)/len(tweets2)))

# percentage of neutral tweets

print("Neutral tweets percentage: {} % \ ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))

print("Neutral tweets after pre-processing percentage Modi: {} % \ ".format(100*(len(tweets1)-len(ntweets1)-len(ptweets1))/len(tweets1)))

print("Neutral tweets after pre-processing percentage Rahul: {} % \ ".format(100*(len(tweets2)-len(ntweets2)-len(ptweets2))/len(tweets2)))

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# printing first 100 positive tweets




40
 
print("\n\nPositive tweets Modi:")



for tweet in ptweets1[:1000]:

print(tweet['text'].translate(non_bmp_map))

print("\n\nPositive tweets Rahul:")

for tweet in ptweets2[:1000]:

print(tweet['text'].translate(non_bmp_map))



#	printing first 5 negative tweets print("\n\nNegative tweets Modi:") for tweet in ntweets1[:1000]:

print(tweet['text'].translate(non_bmp_map)) print("\n\nNegative tweets Rahul:")

for tweet in ntweets2[:1000]: print(tweet['text'].translate(non_bmp_map))

plt.title('View towards Narendra Modi') labels = ['Positive', 'Negative', 'Neutral']
sizes=

[format(100*len(ptweets1)/len(tweets1)),format(100*len(ntweets1)/len(twee ts1)),format(100*(len(tweets1)-len(ntweets1)-len(ptweets1))/len(tweets1))]

colors = ['yellowgreen', 'gold', 'lightskyblue']

patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)

plt.legend(patches, labels, loc="best")

plt.axis('equal')

plt.tight_layout()

plt.show()

plt1.title('View towards Rahul Gandhi')




41
 
labels1 = ['Positive', 'Negative', 'Neutral']

sizes1 = [format(100*len(ptweets2)/len(tweets2)),format(100*len(ntweets2)/len(twee ts2)),format(100*(len(tweets2)-len(ntweets2)-len(ptweets2))/len(tweets2))]

colors1 = ['green', 'red', 'skyblue']

patches1, texts1 = plt1.pie(sizes1, colors=colors1, shadow=True, startangle=90)

plt1.legend(patches1, labels1, loc="best")

plt1.axis('equal')

plt1.tight_layout()

plt1.show()

if __name__ == "__main__":

#	calling main function main()

