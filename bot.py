import tweepy

import json
import os
import sys

from grammar import execute

def send_tweet(credential: dict):
   client = tweepy.Client(
      consumer_key=credential['consumer_key'],
      consumer_secret=credential['consumer_secret'],
      access_token=credential['access_token'],
      access_token_secret=credential['access_token_secret']
   )

   response = client.create_tweet(text=execute())

with open(sys.argv[1]) as raw_cred:
   cred = json.load(raw_cred)

send_tweet(cred)
