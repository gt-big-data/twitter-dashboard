from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import threading
import consumer
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret!'
socketio = SocketIO(app)


@socketio.on('hello')
def handle_hello(message):
    print message
    emit('goodbye', {'data': 'goodbye'})




@app.route("/")
def hello():
    return "Hello World!"

def send_tweet(ch, method, properties, body):
    socketio.emit('geo', {'data': body})

def run_consumer():
    c = consumer.GeoStreamConsumer(send_tweet)
    c.start_consuming()

if __name__ == '__main__':
    print 'Running on http://localhost:5000/'
    t = threading.Thread(target=run_consumer)
    t.start()
    print 'starting app'
    socketio.run(app)
