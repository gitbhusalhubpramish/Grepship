from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from dotenv import load_dotenv
import os 

load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    secret = os.getenv('SECRET_KEY') # Reading secret key from env
    app.config['SECRET_KEY'] = secret

    db_url = os.getenv('DATABASE_URL', 'sqlite:///grepship.db') # Reading Database Url from env
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url 

    db.init_app(app) # calling 
    CORS(app, origins=["http://localhost:3000"]) # Calling

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
