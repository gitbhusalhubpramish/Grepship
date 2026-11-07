from flask_pymongo import PyMongo
from flask_socketio import SocketIO

mongo = PyMongo()

socketio = SocketIO(cros_allowed_origins="*", async_mode="threading")
