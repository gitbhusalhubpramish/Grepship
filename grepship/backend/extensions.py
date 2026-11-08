from flask_pymongo import PyMongo
from flask_socketio import SocketIO

mongo = PyMongo()

socketio = SocketIO(cors_allowed_origins=["http://localhost:3000"], async_mode="threading")
