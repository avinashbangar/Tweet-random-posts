#Script to tweet about articles written on tutkiun
#Version 1.0 
#Future addition :: 1. object oriented script, 2. should send email when something is not working

import feedparser
import twitter
import random
import bitly


d = feedparser.parse('YOUR SITE RSS FEED')

# Get total number of posts
count = 0

for feed in d.entries:
	count = count + 1
	
# Get random post id
id = random.randint(0,count)

#Call bitly api for shortening api
api = bitly.Api(login = 'LOGIN', apikey = 'API KEY')

#Shorten the url and save it to bitly account
short_url = api.shorten(d.entries[id].link,{'history':1})

# Create the tweet for posting to twitter account
tweet = d.entries[id].title
tweet += ' '
tweet += short_url
#tweet = '<Title> <Link>'
#print tweet

# Call the twitter api
api = twitter.Api()

api = twitter.Api(consumer_key='CONSUMER KEY',consumer_secret='CONSUMER SECRET KEY',access_token_key='ACCESS TOKEN',access_token_secret='ACCESS TOKEN SECRET')

#Post update to twitter
status = api.PostUpdate(tweet)


