import requests

def Check_Login(username, password):
    flask_url = ("http://127.0.0.1:5000/db-beasts/logincred")
    authentication = {
        "username": username,
        "password": password
    }

    response = requests.post(flask_url, json=authentication)
    return response
