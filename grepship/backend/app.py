from flask_cors import CORS # Essential for communication
from extensions import mongo  # Mongo Database
from dotenv import load_dotenv  
from pathlib import Path 
import os 
from flask import Flask, jsonify 
from routes.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)

load_dotenv(Path(__file__).parent / ".env")

def create_app(): # Main function for all work 

    app.config[ "SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["MONGO_URI"] = os.getenv(
        "MONGO_URI", "mongodb://localhost:27017/grepship"
    )

    mongo.init_app(app)

    @app.route("/api/health", methods=['GET'])
    def health_check():
        return jsonify({"status":"ok", "service": "Grepship API"}) 
    
    @app.route("/api/hello", methods=["GET"])
    def hello():
        return jsonify({"message": "hello"})
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT", 5000)), debug=True) # Debugger

# What this file does:

# 1. Loads environment variables from .env (SECRET_KEY, MONGO_URI, PORT)
# Creates a flask app using the "app factory" pattern (create_app())
# Connects the app to MongoDB Atlas via flask-pymongo. 
# Enables CORS so the next.js frontend (localhost:3000) can call this API
# Resisters two endpoints 
# Starts the dev server on port 5000 (or PORT from .env) when run directly. 

# 'python app.py' to run this chunk of code. 
#            Anybody who is watching this code i would like to thank you to all to see my hardwork of research & development. 
# Hemanta-Kandel: Coder
