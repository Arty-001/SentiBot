import os
import re

import tweepy as tw
from requests_oauthlib import OAuth1Session

consumer_key = "FJlEboOOHuPWnP0hiJMcyP5Ue"
consumer_secret = "AV2c7GZjz5pwNN7XNn0KpcFMJpqZpAqClJbT2BMXJ20xRD6qB1"
access_token = "1177853975921430528-cTDbQAyGeo8nXhegDUK49jcU7nqHHs"
access_token_secret = "YzN6sre3uWjxuI0mzdkF0mbgJUL7QUK63TgrkbgypP5vo"

auth = tw.OAuthHandler(consumer_key, consumer_secret, callback=None)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)


search_words = "#wildfires"
date_since = "2018-11-16"

new_search = search_words + " -filter:retweets"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)



def remove_pattern(text, pattern_regex):
    r = re.findall(pattern_regex, text)
    for i in r:
        text = re.sub(i, '', text)
    
    return text
# We are keeping cleaned tweets in a new column called 'tidy_tweets'
tweets_df['tidy_tweets'] = np.vectorize(remove_pattern)(tweets_df['tweets'], "@[\w]*: | *RT*")
