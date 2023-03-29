import re

# Define political keywords, hashtags, and mentions
political_keywords = ['politics', 'election', 'government']
political_hashtags = ['#iranpolitics', '#iranvotes']
political_mentions = ['@iranpolitics']

# Identify political content in tweets
political_tweets = []
for tweet in farsi_tweets:
    text = tweet.text.lower()
    if any(keyword in text for keyword in political_keywords) \
    or any(hashtag in text for hashtag in political_hashtags) \
    or any(mention in text for mention in political_mentions):
        political_tweets.append(tweet)
``
