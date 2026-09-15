from flask import Flask, jsonify
from flask_cors import CORS
from extensions import mongo 
from dotenv import load_dotenv
import os 

load_dotenv()

def create_app():
    app = Flask(__name__)

    secret = os.getenv('SECRET_KEY') # Reading secret key from env
    app.config['SECRET_KEY'] = secret

    db_url = os.getenv('DATABASE_URL', 'sqlite:///grepship.db') # Reading Database Url from env

    CORS(app, origins=["http://localhost:3000"]) # Calling

    app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/grepship')
    mongo.init_app(app)

    @app.route("/api/health", methods=['GET']) # Routing /api/health
    def  health_check():
        return jsonify({'status':"ok","services":"Grepship API"})
    
    @app.route('/api/hello', methods=['GET']) # Routing /api/hello
    def hello():
        return jsonify({"message":"hello"})

    return app 

app = create_app()

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 5000)), debug=True) # If something went wrong flask have a feature to run debugger there automatically. 
