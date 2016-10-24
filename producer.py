import pika
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


class StreamProducer(StreamListener):

    def __init__(self):
        return

    def on_data(self, data):
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    producer = StreamProducer()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, producer)
    stream.sample()
