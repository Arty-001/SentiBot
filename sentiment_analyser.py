from fetch import *
import json
import tweepy,csv,re
from textblob import TextBlob

class SentimentAnalysis:

    def __init__(self):
        self.tweets = []

    def DownloadData(self):

        polarities=[]
        positive_tweets = []
        negative_tweets = []

        f = open("tweet.json")
        data = json.load(f)
        p,n = 0,0
        for i in range(100):
            analysis = TextBlob(data[str(i)])
            if (analysis.sentiment.polarity > 0):
                if p<10:
                    positive_tweets.append(data[str(i)])
                polarities.append(analysis.sentiment.polarity)
                p+=1
            elif analysis.sentiment.polarity ==0:
                polarities.append(analysis.sentiment.polarity)
            elif (analysis.sentiment.polarity < 0):
                if n<10:
                    negative_tweets.append(data[str(i)])
                polarities.append(analysis.sentiment.polarity)
                n+=1
        try:
            with open(r"timeByTime.csv",'w',encoding="utf-8",newline='') as file:
                writer = csv.writer(file)
                writer.writerows(map(lambda x: [x],polarities))
            with open(r"positiveTweets.csv",'w',encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(positive_tweets)
            with open(r"negativeTweets.csv",'w',encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(negative_tweets)
            print("Data saved for analysis")
        except Exception as e:
            print("Some error occured :(")
            print(e)

def main(text):
    json_maker(text)
    sa = SentimentAnalysis()
    sa.DownloadData()