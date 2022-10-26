'''
Example script to collect 'Because of ...#MahsaAmini' Tweets in persian with the Twitter Premium Search API
To use this script, change the constants (UPPERCASE variables) to your needs,
and run it.
Find your app credentials here: https://developer.twitter.com/en/apps
Find your dev environment label here: https://developer.twitter.com/en/account/environments
'''
API_KEY = 'XXXX'
API_SECRET_KEY = 'XXXX'
DEV_ENVIRONMENT_LABEL = 'XXXX'
API_SCOPE = '30day'  # 'fullarchive' for full archive, '30day' for last 31 days

SEARCH_QUERY = 'برای''#مهساـامینی'
RESULTS_PER_CALL = 100  # 100 for sandbox, 500 for paid tiers
TO_DATE = '2022-10-1' # format YYYY-MM-DD HH:MM (hour and minutes optional)
FROM_DATE = '2022-09-20'  # format YYYY-MM-DD HH:MM (hour and minutes optional)

MAX_RESULTS = 10000000  # Number of Tweets you want to collect

FILENAME = 'Because_of-tweets.jsonl'  # Where the Tweets should be saved

# Script prints an update to the CLI every time it collected another X Tweets
PRINT_AFTER_X = 1000

#--------------------------- STOP -------------------------------#
# Don't edit anything below, if you don't know what you are doing.
#--------------------------- STOP -------------------------------#

import yaml
config = dict(
    search_tweets_api=dict(
        account_type='premium',
        endpoint=f"https://api.twitter.com/1.1/tweets/search/{API_SCOPE}/{DEV_ENVIRONMENT_LABEL}.json",
        consumer_key=API_KEY,
        consumer_secret=API_SECRET_KEY
    )
)

with open('twitter_keys.yaml', 'w') as config_file:
    yaml.dump(config, config_file, default_flow_style=False)

    
import json
from searchtweets import load_credentials, gen_rule_payload, ResultStream

premium_search_args = load_credentials("twitter_keys.yaml",
                                       yaml_key="search_tweets_api",
                                       env_overwrite=False)

rule = gen_rule_payload(SEARCH_QUERY,
                        results_per_call=RESULTS_PER_CALL,
                        from_date=FROM_DATE,
                        to_date=TO_DATE
                        )

rs = ResultStream(rule_payload=rule,
                  max_results=MAX_RESULTS,
                  **premium_search_args)

with open(FILENAME, 'a', encoding='utf-8') as f:
    n = 0
    for tweet in rs.stream():
        n += 1
        if n % PRINT_AFTER_X == 0:
            print('{0}: {1}'.format(str(n), tweet['created_at']))
        json.dump(tweet, f)
        f.write('\n')
print('done')