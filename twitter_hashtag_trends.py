"""
Note that in order to use this script, you'll need to create a Twitter Developer account and obtain API credentials. 
You can find more information on how to do that here: 
https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api
"""


import tweepy

# Set up the Twitter API client
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the top 10 Twitter trends
trends = api.trends_place(1)[0]['trends'][:10]

# Choose the best hashtag based on the number of tweets
best_hashtag = max(trends, key=lambda x: x['tweet_volume'])['name']

print('The best hashtag of the moment is:', best_hashtag)
