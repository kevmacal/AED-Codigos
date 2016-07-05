# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

import json

consumer_key = "Obtener de Twitter"
consumer_secret = "Obtener de Twitter"
access_token = "Obtener de Twitter"
access_token_secret = "Obtener de Twitter"
file_raw = open('./data/dataStreamChicago_' + time.strftime('%Y%m%d') + '.json', 'a')


#Listener para cada tweet que se recibe
class StdOutListener(StreamListener):
    def __init__(self):
        self.contTweets = 0

    def on_data(self, data):
        tweet = json.loads(data)
        #print (str(tweet['coordinates']))
        #print (tweet['text'])
        if tweet['coordinates']:
            file_raw.write(data)
            self.contTweets = self.contTweets + 1
            print (("Tweet Chicago Coordinates:" + str(tweet['coordinates']) + "Numero: " + str(self.contTweets) + "\nTexto: " + tweet['text'] + "\n"))
        return True

    def on_error(self, status_code):
        if status_code == 429:
            print (status_code)
            print ("Exceed rate limit")
            time.sleep(60 * 5)
            return True  # En este caso se debe mantener, solo hacer una pausa de 5 minutos y volver a intentar
        elif status_code == 420:
            print (status_code)

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, StdOutListener())
#    stream.filter(locations=[-124.482009887695, 32.5295219421387, -114.13077545166, 42.0095024108887,]) California
    stream.filter(locations=[-87.939195, 41.656424, -87.531348, 42.019607])  # Chicago


    # 41.656424, -87.939195 , 42.019607, -87.531348  Chicago
