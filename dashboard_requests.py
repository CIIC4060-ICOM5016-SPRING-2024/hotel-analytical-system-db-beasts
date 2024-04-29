import requests
from config.db import DatabaseOption


def Check_Login(username, password):
    flask_url = 0
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/login/voila"
    elif DatabaseOption() == 'h':
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/login/voila"
    credentials = {'username': username, 'password': password}
    response = requests.post(flask_url, json=credentials)
    return response


def Check_Employee(eid, fname, lastname):
    flask_url = 0
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/employee/voila"
    elif DatabaseOption() == 'h':
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/employee/voila"
    data = {'eid': eid, 'fname': fname, 'lname': lastname}
    response = requests.post(flask_url, json=data)
    return response


def Post_Login(eid, username, password):
    flask_url = 0
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/login"
    elif DatabaseOption() == 'h':
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/login"
    data = {'eid': eid, 'username': username, 'password': password}
    response = requests.post(flask_url, json=data)
    return response


def Get_Employee(eid):
    flask_url = 0
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/employee/{eid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/employee/{eid}"
    response = requests.get(flask_url)
    return response
