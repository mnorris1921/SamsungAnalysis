import tweepy
# auth.py should contain yeach of your 4 oauth elements (1 per line)
# API key means the same thing as consumer key
# DO NOT push your own keys to the repo! 
from auth import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'samsung'
max_tweets = 1000
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

# now we do stuff with searched_tweets