import tweepy 
from tweepy import Stream
from tweepy.streaming import StreamListener 
import json
import time
import datetime


#Streamer Class


class MyListener(StreamListener):
    def __init__(self, api, file_name_base):
        self.tweet_list=[]
        self.count = 1
        self.file_name_base = file_name_base
       
    def on_data(self, data):
        try:
            j = json.loads(data)
            self.tweet_list.append(j)
            n = len(self.tweet_list)


            if (n % 500 == 0):
                ts = time.time()
                stamp = datetime.datetime.fromtimestamp(ts).strftime('%m%d%H%M%S')
                file_name = self.file_name_base + stamp + '.json'
                with open(file_name , 'w') as f:
                    json.dump(self.tweet_list, f)
                print("Output File", self.count)
                self.count = self.count + 1
                self.tweet_list = []
            return True
        except BaseException as e:
            print("Error on_data:", str(e))
        return True
 
    def on_error(self, status):
        print("Error",status)
        return False

class Credentials:
    def __init__(self, access_token, access_token_secret, consumer_key, 
        consumer_secret):
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret


def mine_tweets(credentials, search_terms, file_name):
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)

    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener(auth, file_name))

    print("Starting up!")

    while(True):
        try:
            twitter_stream.filter(track=search_terms)
        except:
            time.sleep(30)
            print("program restart")


 
