import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

BEARER_TOKEN        = os.getenv('BEARER_TOKEN')
API_KEY             = os.getenv('API_KEY')
API_SECRET          = os.getenv('API_SECRET')
ACCESS_TOKEN        = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                       consumer_key    = API_KEY,
                       consumer_secret = API_SECRET,
                       access_token    = ACCESS_TOKEN,
                       access_token_secret = ACCESS_TOKEN_SECRET,
                      )
    


res = client.create_tweet(text="test")
print(res)