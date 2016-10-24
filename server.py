from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

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

if __name__ == '__main__':
    print 'Running on http://localhost:5000/'
    socketio.run(app)
