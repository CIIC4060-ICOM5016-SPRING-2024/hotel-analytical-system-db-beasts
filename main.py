from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the hotel-analytical-system-db-beasts app'


if __name__ == '__main__':
    app.run()
