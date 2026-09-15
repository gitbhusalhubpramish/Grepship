from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000/"])

@app.get("/api/hello")
def hello():
	return {
		"message": "hello"
	}

if __name__ == "__main__":
	app.run(port=5000,debug=True)
