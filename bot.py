import tweepy
import os

from grammar import execute

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

def send_tweet():
   client = tweepy.Client(
      consumer_key=consumer_key,
      consumer_secret=consumer_secret,
      access_token=access_token,
      access_token_secret=access_token_secret
   )

   response = client.create_tweet(text=execute())
