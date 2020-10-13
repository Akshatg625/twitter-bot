# Python Twitter bot
# Made by: Akshat Gupta+ Ashwani Rathee
# Using Twitter API

import tweepy
import pandas as pd
from time import sleep  # to manage mean time when there is nothing to do
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME
import csv

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def botSettings():
    print("Twitter bot which retweets, like tweets and follow users")
    print("Bot Settings")
    print("Like Tweets :", LIKE)
    print("Follow users :", FOLLOW)


def retweetAndFollow():
    for tweet in tweepy.Cursor(api.search, q=QUERY, lang='en').items(3):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print("User Details:")
            print(tweet.created_at)
            print(tweet.user.id)
            print(tweet.user.name)
            print(tweet.user.description)
            print(tweet.user.location)
            print("last 2 followers:")
            for follower in tweepy.Cursor(api.followers, tweet.user.screen_name).items(2):
                print(follower.name)
            print(tweet.text)
            tweet.retweet()
            print('Retweeted the tweet')

            # Favorite the tweet
            if LIKE:
                tweet.favorite()
                print('Favorited the tweet')
            # Follow the user who tweeted
            # check that bot is not already following the user
            if FOLLOW:
                if not tweet.user.following:
                    tweet.user.follow()
                    print('Followed the user')
            print("----------X---------")

            sleep(SLEEP_TIME)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


def trending():
    for tweet in tweepy.Cursor(api.search, q=QUERY, lang='en', result_type='popular').items(3):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print("User Details:")
            print(tweet.created_at)
            print(tweet.user.name)
            print(tweet.user.description)
            print(tweet.user.location)
            print(tweet.text)
            print("----------X---------")

            sleep(SLEEP_TIME)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


def findID(user_name):
    statuses = api.user_timeline(screen_name = user_name, count = 200)
    tweets=[]
    tweets.extend(statuses)
    # for status in statuses:
    #     print(status.text)
    #     print("------------------------")
    # save the id of the oldest tweet less one
    oldest = tweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(statuses) > 0:
        statuses = api.user_timeline(screen_name = user_name, count = 200, max_id=oldest)
        # save most recent tweets
        tweets.extend(statuses)

        # update the id of the oldest tweet less one
        oldest = tweets[-1].id - 1

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
    with open(f'{user_name}_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
        x=pd.read_csv(f'{user_name}_tweets.csv')
        x.dropna(axis=0,how='any',inplace=True)
        x.to_csv('file.csv')
    print("Done")

def choice():
    global QUERY
    ch = int(input("""
    1) Automatic retweet, like and follow
    2) Find trending
    3) Hashtags to search
    4) Find people and information about them
    """))
    if ch == 1:
        retweetAndFollow()
    elif ch == 2:
        trending()
    elif ch == 3:
        QUERY = '#' + input()
        choice()
    elif ch == 4:
        user_name = input("Input screen name")
        findID(user_name)


def main():
    choice()


if __name__ == "__main__":
    main()



# # fetching the user
#     user = api.get_user(user_name)

#     # fetching the ID
#     ID = user.id_str