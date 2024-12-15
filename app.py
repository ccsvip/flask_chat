import os
from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.secret_key = os.urandom(64)

@app.get("/")
def index():
    return render_template("index.html")

if  __name__ == "__main__":
    socketio.run(app, debug=True, port=8888)