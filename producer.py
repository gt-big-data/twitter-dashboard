import json

import pika
from twython import TwythonStreamer


def load_credentials(_file):
    with open(_file, 'r') as f:
        return json.loads(f.read())


class StreamProducer(TwythonStreamer):

    def __init__(self, app_key, app_secret, access_token, access_token_secret):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='tweets', type='fanout')
        super(StreamProducer, self).__init__(app_key, app_secret, access_token, access_token_secret)
        return

    def on_success(self, data):
        self.channel.basic_publish(exchange='tweets', routing_key='', body=json.dumps(data))
        return

    def on_error(self, status_code, data):
        if status_code == 420:
            print 'Being rate limited, disconnecting.'
            return self.disconnect()

if __name__ == '__main__':
    """
    You'll need a credentials.json in the same directory. It should be
    of the form:
    {
     "API_KEY" : "XXXXXX",
     "API_SECRET" : "XXXXXX",
     "ACCESS_TOKEN" : "XXXXXX",
     "ACCESS_TOKEN_SECRET" : "XXXXXX"
     }
    """
    credentials = load_credentials('credentials.json')
    api_key = credentials['API_KEY']
    api_secret = credentials['API_SECRET']
    access_token = credentials['ACCESS_TOKEN']
    access_token_secret = credentials['ACCESS_TOKEN_SECRET']
    stream = StreamProducer(api_key, api_secret, access_token, access_token_secret)
    print 'Starting producer'
    stream.statuses.filter(locations=['-180,-90', '180,90'])
