from flask_cors import CORS # Essential for communication
from extensions import mongo, socketio  # Mongo Database
from dotenv import load_dotenv  
from pathlib import Path 
import os 
from flask import Flask, jsonify 
from routes.auth import auth_bp
from routes.messages import inb_bp
from flask_socketio import SocketIO
from extensions import mongo

load_dotenv(Path(__file__).resolve().parent.parent/".env")


def create_app(): # Main function for all work 
    app = Flask(__name__)
    socketio.init_app(app)
    #app.config[ "SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["MONGO_URI"] = os.getenv("MONGODB_URI")
    mongo.init_app(app)
    print(mongo)
    print(mongo.db)

    CORS(app, origins=['http://localhost:3000'], supports_credentials=True)
    app.register_blueprint(auth_bp)
    app.register_blueprint(inb_bp)

    @app.route("/api/health", methods=['GET'])
    def health_check():
        return jsonify({"status":"ok", "service": "Grepship API"}) 
    
    @app.route("/api/hello", methods=["GET"])
    def hello():
        return jsonify({"message": "hello"})
    
    return app

app = create_app()

if __name__ == '__main__':
    socketio.run(app,port=int(os.getenv("PORT", 5000)), debug=True) # Debugger
