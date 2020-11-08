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
            analysis = TextBlob(data[i])
            
            if (analysis.sentiment.polarity >= 0):
                if p<10:
                    positive_tweets.append(data[i])
                polarities.append(1)
                p+=1
            elif (analysis.sentiment.polarity < 0):
                if n<10:
                    negative_tweets.append(data[i])
                polarities.append(0)
                n+=1
                
        with open(r"timeByTime.csv",'w',encoding="utf-8",newline='') as file:
            writer = csv.writer(file)
            writer.writerows(map(lambda x: [x],polarities))
        with open(r"positiveTweets.csv",'w',encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(positive_tweets)
        with open(r"negativeTweets.csv",'w',encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(negative_tweets)
        #print(len(polarities))
        

if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()