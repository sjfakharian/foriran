from textblob import TextBlob

# Get sentiment polarity of each tweet using TextBlob
sentiments = [TextBlob(tweet.text).sentiment.polarity for tweet in farsi_tweets]
