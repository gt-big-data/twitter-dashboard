import pika
import json


class StreamConsumer(object):

    def __init__(self, callback):
        self.callback = callback
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='tweets', type='fanout')
        self.result = self.channel.queue_declare(exclusive=True)
        self.channel.queue_bind(exchange='tweets', queue=self.result.method.queue)
        return

    def start_consuming(self):
        self.channel.basic_consume(self.callback, queue=self.result.method.queue, no_ack=True)
        self.channel.start_consuming()
        return

if __name__ == '__main__':

    def noop(ch, method, properties, body):
        print body

    consumer = StreamConsumer(noop)
    consumer.start_consuming()
