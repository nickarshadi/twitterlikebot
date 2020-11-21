#!/usr/bin/python3
"""Use python API."""

import tweepy
import time

"""Here insert your twitter api public key and private key"""
auth = tweepy.OAuthHandler("[your public key]", "[your private key]")
"""Here insert your private and public twitter api token."""
auth.set_access_token('[your public token]', '[Your private token]')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

"""Here insert the keyword to seach for."""
search = '100daysofcode'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
