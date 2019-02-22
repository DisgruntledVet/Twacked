import tweepy
import csv #Import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import requests
#you must have twitter api keys to run this you do this by creating a app on twitter you can follow directions here 
#you must have two terminal windows open for this to work one servedup.py will be ran and the other getem.py 
#you want to look at certain tweets by date and search terms look no further i have the solution all you need to do is pip install tweepy 
#from tweepy you are able to call twitters api and print data into your console i created this to write in a csv so i can temporarily use as a database.
#that csv file/ temp database will later be called in servedup.py to be beautified on a server with html and css
# what content does this look for and what exactly does it print? you ask it prints off the date the tweet is created and the text in that tweet 

# put your two keys here in this order consumer_key, consumer_secret
auth = tweepy.auth.OAuthHandler('Consumer Key Here','Consumer Secret here')
# put your two tokens here in this order access_token, access_token_secret
auth.set_access_token('Access token here', 'acess secret token here')

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('hacked.csv', 'a')
#csvFile = open('great.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
#put in the dates you would like to look for tweets with the word hacked
for tweet in limit_handled(tweepy.Cursor(api.search,
							
                           	q = "hacked",
                           	since = "year-month-day",
                           	until = "year-month-day",
                           	lang = "en").items()):

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text, 
csvFile.close()



