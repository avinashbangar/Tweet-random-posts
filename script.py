#Script to tweet about articles written on tutkiun
#Version 1.0 
#Future addition :: 1. Should send email when something is not working

import feedparser
import twitter
import random
import bitly


class RandomTweet:
    'Class for Posting Random Tweets from a blog post'
    
    def generate_tweet(self):
    
        feeds = feedparser.parse('SITE RSS FEED LINK')
        # Get total number of posts
        count = 0

        for feed in feeds.entries:
	        count = count + 1
	
        # Get random post id
        id = random.randint(0,count)

        #Call bitly api for shortening api
        api = bitly.Api(login = 'LOGIN', apikey = 'API KEY')

        #Shorten the url and save it to bitly account
        short_url = api.shorten(feeds.entries[id].link,{'history':1})

        # Create the tweet for posting to twitter account
        tweet = feeds.entries[id].title
        tweet += ' '
        tweet += short_url

        #print tweet

        return tweet

    def post_to_twitter(self,tweet):
        # Call the twitter api
        api = twitter.Api()

        api = twitter.Api(consumer_key='COSUMER KEY',consumer_secret='CONSUMER SECRET KEY',access_token_key='ACCESS TOKEN KEY',access_token_secret='ACCESS TOKEN SECRET')

        #Post update to twitter
        status = api.PostUpdate(tweet)

        return


obj = RandomTweet()

tweet = obj.generate()
obj.post_to_twitter(tweet)


