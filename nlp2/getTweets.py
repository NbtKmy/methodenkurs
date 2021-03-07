import tweepy
import pandas as pd
import re
import MeCab

# Your API keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# Auth-Instanzen erstellen
def authTwitter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    return api


# get 50 items with keyterm 
def getTweetsBySearch(term):
    api = authTwitter()


    tweets = tweepy.Cursor(api.search, q = term, \
        include_entities = True, \
        tweet_mode = 'extended', \
        lang = 'ja').items(1000)

    tweetsList = []
    corpus = ""
    for tweet in tweets:
        # user-id, url, hash-tag, Zeilenumbruch und Spatien aus dem Tweets entfernen
        a = re.sub(r'@.*','', tweet.full_text)
        b = re.sub(r'http.*','', a)
        c = re.sub(r'#.*', '', b)
        d = re.sub(r'\n','', c)
        e = re.sub(r'\s+','', d)
        tweetsList.append([e, tweet.favorite_count, tweet.retweet_count])
        corpus += e

    tweetsDf = pd.DataFrame(tweetsList, columns=['text', 'favorite counts', 'retweet counts'])
    tweetsDf.to_csv('tweetsdata.csv', encoding='utf_8')

    



if __name__ == "__main__":
    getTweetsBySearch('オリンピック -filter:retweets')
