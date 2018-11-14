import tweepy 
from tweepy import Stream
from tweepy.streaming import StreamListener 
import json
import time
import datetime
from twitter_miner import *

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''



text_list = ['MPOB', 'palm oil', 'oil palm', 'palmoil', 'palm oil plantations', 'rspo', 'palm olie', 'palmolie', "Palm Oil", "RSPO", 'minyak kelapa sawit', "aceite de palma"] 
hashtag_list = ['#palmoil', '#oilpalm', '#rspo', '#RefinedPalmOil', '#palmolie']
mentions_list = []
mentions_list = []
from_list = []
to_list = []

full_list = text_list
full_list.extend(hashtag_list)
full_list.extend(mentions_list)
full_list.extend(from_list)
full_list.extend(to_list)


credentials = Credentials(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET)

# this is the path that the files will save to your computer.
file_name_base = '/root/tweet-files/'

#starting the program
mine_tweets(credentials, full_list, file_name_base)




