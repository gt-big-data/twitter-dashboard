from flask import Flask
from flask_socketio import SocketIO
from consumer import StreamConsumer
import threading
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret!'
socketio = SocketIO(app)


def emit_coordinates(ch, method, properties, body):
    socketio.emit('coordinates', {'data': json.loads(body)})
    return

def emit_trending_list(ch, method, properties, body):
    socketio.emit('trending', {'data': json.loads(body)})
    return

def run_consumer(callback):
    c = StreamConsumer(callback)
    c.start_consuming()
    return

if __name__ == '__main__':
    print 'Running on http://localhost:5000/'
    coordinates_thread = threading.Thread(target=run_consumer, args=(emit_coordinates,))
    coordinates_thread.daemon = True
    coordinates_thread.start()
    trending_thread = threading.Thread(target=run_consumer, args=(emit_trending_list,))
    trending_thread.daemon = True
    trending_thread.start()
    print 'starting app'
    socketio.run(app)
