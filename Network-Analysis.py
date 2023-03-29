import networkx as nx

# Create directed graph of retweets
retweet_graph = nx.DiGraph()
for tweet in farsi_tweets:
    if hasattr(tweet, 'retweeted_status'):
        user = tweet.author.screen_name
        retweeter = tweet.retweeted_status.author.screen_name
        retweet_graph.add_edge(user, retweeter)

# Get degree centrality of users
degree_centrality = nx.degree_centrality(retweet_graph)
