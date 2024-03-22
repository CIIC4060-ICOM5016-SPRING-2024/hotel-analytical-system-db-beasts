from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# apply CORS
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the hotel-analytical-system-db-beasts app'


if __name__ == '__main__':
    app.run(debug=True)
