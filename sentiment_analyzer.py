import json
import tweepy,csv,re
from textblob import TextBlob

class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def cleanTweet(self, tweet):
        tweet = tweet.lower() # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
        tweet = ''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split()) # remove usernames
        return tweet

    def DownloadData(self, searchTerm):

        polarities=[]
        positive_tweets = []
        negative_tweets = []

        f = open("sample.json")
        data = json.load(f)
        # for i in range(100):
        #     print(data[str(i)])
        p,n = 0,0
        # iterating through tweets fetched
        for i in range(100):
            #Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(data[str(i)]).encode('utf-8'))
            analysis = TextBlob(data[str(i)])
            #polarity += analysis.sentiment.polarity  # adding up polarities to find the average later
            
            if (analysis.sentiment.polarity >= 0):
                if p<10:
                    positive_tweets.append(data[str(i)])
                polarities.append(1)
                p+=1
            elif (analysis.sentiment.polarity < 0):
                if n<10:
                    negative_tweets.append(data[str(i)])
                polarities.append(0)
                n+=1
        # print("\n Positive tweets")
        # print(positive_tweets)
        # print("\n\n Negative tweets")
        # print(negative_tweets)
        with open(r"timeByTime.csv",'w',encoding="utf-8") as file:
            writer = csv.writer(file)
            t = range(1,101)
            writer.writerow(t)
            writer.writerow(polarities)
        with open(r"positiveTweets.csv",'w',encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(positive_tweets)
        with open(r"negativeTweets.csv",'w',encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(negative_tweets)
        print(len(polarities))
        # print(self.tweetText, polarities)
        
        # with open("TopTweets.csv",'w',newline='') as file:
        #     writer = csv.writer(file)
        #     writer.


if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData("Us election")