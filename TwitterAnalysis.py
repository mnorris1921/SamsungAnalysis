import tweepy
# auth.py should contain yeach of your 4 oauth elements (1 per line)
# API key means the same thing as consumer key
# DO NOT push your own keys to the repo! 
from auth import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

f = open('tweets.txt', 'w+')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'samsung'
max_tweets = 1000

api.wait_on_rate_limit = True
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

print(type(searched_tweets))
print(type(searched_tweets[0]))

i=0
# now we do stuff with searched_tweets
for tweet in searched_tweets:
   f.write(str(i))
   i=i+1
   f.write("\n")
   f.write(tweet.text.encode('utf-8'))
   f.write("\n\n\n")