import tweepy as tp
import time
import os


consumer_key = 'AHDPRwJtdAh12FTdoepiu48xw'
consumer_secret = 'Z1AbHwu0vHqjZ6B01rsxKgs5xEeAyDRutlpKVVvUDdhwmJ5NC4'
access_token = '1181276838481391619-AU4XQoPGeYgT7ivPk3Wr5RLbiIlZCy'
access_secret = 'zFq7BfcIbTCxUMz6YF6uy9iUYpPoRiNYNSImBYMyYXAq7'

auth = tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)

os.chdir('wallp')
for wall in os.listdir('.'):
    api.update_with_media(wall)
    time.sleep(5)