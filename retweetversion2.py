import tweepy
import json
import time
 
def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
 
    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token,       access_token_secret)
 
    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return  api


def retweet(api, tweet_id):
    success = False
    try:
        a= api.retweet(tweet_id)
 
        # Sleep for 2 seconds, Thanks Twitter
        print("Sleeping for 5 seconds")
        time.sleep(5)
        success = True
    except tweepy.TweepError as e:
        a=e.response.text
        b=json.loads(a)
        error_code = b['errors'][0]['code']
 
        if(error_code == 327):
            success = True
 
    return success

def post_tweets():
	consumer_key= "hKb5wLh17wuZEYuYkZsf9R8QM"
	consumer_secret	= "nRQgpsid6dWfDoCGsF2DJMJPQEt3y8XJMCZ3YzbBWKgb0wgbxg"
	access_token =  "615327272-HsCGG0bydM0Y8KhJ4F1GxiQJmQdr8sTN0UFWMj7V"
	access_token_secret="WKDpVKRUmdD4Tpx2H45KztnyOvboXEfC1OwMseCU86X1B"
	api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret )
	query = "#saveNITAPstudents"
	tweet_cursor = tweepy.Cursor(api.search, query, result_type="recent", include_entities=True, lang="en").items()
	for tweet in tweet_cursor:
		tweet_id = tweet.id_str
		retweet(api, tweet_id)

 
 
if __name__ == '__main__':
    post_tweets()