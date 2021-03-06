from heads import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
