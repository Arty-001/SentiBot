import sys
import os
import re
import tweepy as tw
# from requests_oauthlib import OAuth1Session
import csv
import json
from geopy.geocoders import Nominatim

def divider(text):
    check = re.search(";",text)
    if check:
        x = text.split(";")
        keyword = x[0]
        location= x[1]
    else:
        keyword=text
        location=''
    return keyword, location

def get_coordinates(region):
    if region!='':
        geolocator = Nominatim(user_agent="SentiBot")
        location = geolocator.geocode(region)
        return location.longitude, location.latitude
    else:
        return ''

def get_auth():
    consumer_key = "ydKKAoXFmqq97PZWYPs4wfy5S"
    consumer_secret = "G1tFaa0Gop0kGCYsZzUpx1RLYjvIFv8qwS9H5dreZkgqlfCEnR"
    access_token = "856759533640622080-HhlrgshaitB8gR2TXvrBq60XtNeRnXP"
    access_token_secret = "8GYPov3JIJAJD8o2PvkGtdrXwUy5HewqEOXeTdAwKZP5Q"

    auth = tw.OAuthHandler(consumer_key, consumer_secret, callback=None)
    auth.set_access_token(access_token, access_token_secret)
    try:
        api = tw.API(auth)
        print("Authentication successful")
        return api
    except Exception as e:
        print("Authentication failed")
        print(e)
        sys.exit()


def json_maker(text):
    api = get_auth()
    search_words,region = divider(text)
    date_since = "2018-11-16"

    new_search = search_words + " -filter:retweets"
    item = 100
    if region!='':
        longi, lati = get_coordinates(region)
        coordinates=str(longi)+","+str(lati)+",500mi"
    else:
        coordinates=''
    tweets = tw.Cursor(api.search,
                q=new_search, tweet_mode = 'extended',
                lang="en",
                geocode=coordinates,
                since=date_since).items(item)
    twe_dict = {}
    key = range(100)
    tweet_dict = [tweet.full_text for tweet in tweets]
    for i in key:
        twe_dict[i] = tweet_dict[i]
    with open("tweet.json", "w") as outfile: 
        json.dump(twe_dict, outfile) 
    
    print("Json file created")