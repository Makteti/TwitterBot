from time import sleep
import tweepy
import config
#using config file, given that access is granted.
client = tweepy.Client(consumer_key = config.API_KEY,
consumer_secret = config.API_Secret,
access_token = config.ACCESS_TOKEN,
access_token_secret = config.ACCESS_TOKEN_SECRET)
#Splitting Parsing files to single instance; hard-encoding to utf-8, bugs before
with open("TwitterBot\Quotes.txt", "r", encoding="utf8") as quotes:
    lines = quotes.read()
    results = lines.split("\n\n")
    n = 0
    for x in results:
        try:
            client.create_tweet(text = results[n])
            n += 1
            sleep(15)
        except tweepy.errors.BadRequest:
            print("tweepy.errors.BadRequest: Quote too long") #tweepy.errors.BadRequest: 400 Bad Request
            n += 1
