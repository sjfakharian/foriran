import gensim
from gensim import corpora

# Create dictionary and corpus of stemmed tokens
dictionary = corpora.Dictionary(stemmed_tokens)
corpus = [dictionary.doc2bow(tweet_tokens) for tweet_tokens in stemmed_tokens]

# Train LDA model and print topics
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, passes=10)
topics = lda_model.print_topics(num_words=5)
print(topics)
