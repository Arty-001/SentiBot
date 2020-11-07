import os
import tweepy as tw
#import pandas as pd

consumer_key = "ydKKAoXFmqq97PZWYPs4wfy5S"
consumer_secret = "G1tFaa0Gop0kGCYsZzUpx1RLYjvIFv8qwS9H5dreZkgqlfCEnR"
access_token = "856759533640622080-HhlrgshaitB8gR2TXvrBq60XtNeRnXP"
access_token_secret = "8GYPov3JIJAJD8o2PvkGtdrXwUy5HewqEOXeTdAwKZP5Q"

auth = tw.OAuthHandler(consumer_key, consumer_secret, callback=None)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

search_words = "byjus"
date_since = "2018-11-16"

new_search = search_words + " -filter:retweets"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since).items(100)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)