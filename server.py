from flask import Flask
from flask_socketio import SocketIO
import threading
from consumer import StreamConsumer
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret!'
socketio = SocketIO(app)


def emit_coordinates(ch, method, properties, body):
    socketio.emit('coordinates', {'data': body})

def emit_trending_list(ch, method, properties, body):
    socketio.emit('trending', {'data': body})

def run_consumer_with_callback(callback):
    c = StreamConsumer(callback)
    c.start_consuming()

if __name__ == '__main__':
    print 'Running on http://localhost:5000/'
    coordinates_thread = threading.Thread(target=run_consumer_with_callback, args=(emit_coordinates))
    coordinates_thread.start()
    trending_thread = threading.Thread(target=run_consumer_with_callback, args=(emit_trending_list))
    trending_thread.start()
    print 'starting app'
    socketio.run(app)
