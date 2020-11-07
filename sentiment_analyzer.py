import json
from textblob import TextBlob

y= input("Sentence: ")
analyzer = TextBlob(y)
x = analyzer.sentiment.polarity

if x<0:
    print("Negative")
elif x==0:
    print("Neutral")
else:
    print("Positive")