import hazm
from persian_stemmer import Stemmer

# Tokenize tweets using Hazm
tokenizer = hazm.TweetTokenizer()
tokens = [tokenizer.tokenize(tweet.text) for tweet in farsi_tweets]

# Stem tokens using PersianStemmer
stemmer = Stemmer()
stemmed_tokens = [[stemmer.stem(token) for token in tweet_tokens] for tweet_tokens in tokens]
