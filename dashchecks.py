"""
-----------------------------------------------------------------------------------------------------------------------
Region Imports
-----------------------------------------------------------------------------------------------------------------------
"""

import requests
from config.db import DatabaseOption

"""
-----------------------------------------------------------------------------------------------------------------------
Region Dashboard
-----------------------------------------------------------------------------------------------------------------------
"""


def Check_Login(username, password):
    flask_url = "http://127.0.0.1:5000/db-beasts/logincred"
    authentication = {
        "username": username,
        "password": password
    }

    response = requests.post(flask_url, json=authentication)
    return response

def Post_LogIn(eid, username, password):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/login"
    elif DatabaseOption() == 'h':
        pass
    data = {'eid': eid, 'username': username, 'password': password}
    response = requests.post(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Crud
-----------------------------------------------------------------------------------------------------------------------
"""
"""
-----------------------------------------------------------------------------------------------------------------------
Region Chain
-----------------------------------------------------------------------------------------------------------------------
"""


def Post_Chain(cname, fallmkup, springmkup, summermkup, wintermkup):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/chains"
    elif DatabaseOption() == 'h':
        pass
    data = {'cname': cname, 'fallmkup': fallmkup, 'springmkup': springmkup, 'summermkup': summermkup,
            'wintermkup': wintermkup}
    response = requests.post(flask_url, json=data)
    return response


def Delete_Chain(chid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/chains/{chid}"
    elif DatabaseOption() == 'h':
        pass
    response = requests.delete(flask_url)
    return response


def Put_Chain(chid, cname, fallmkup, springmkup, summermkup, wintermkup):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/chains/{chid}"
    elif DatabaseOption() == 'h':
        pass
    data = {'cname': cname, 'fallmkup': fallmkup, 'springmkup': springmkup, 'summermkup': summermkup,
            'wintermkup': wintermkup}
    response = requests.put(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Client
-----------------------------------------------------------------------------------------------------------------------
"""
def Post_Client(fname, lname, age, memberyear):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/client"
    elif DatabaseOption() == 'h':
        pass
    data = {'fname': fname, 'lname': lname, 'age': age, 'memberyear': memberyear}
    response = requests.post(flask_url, json=data)
    return response

def Delete_Client(cid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/client/{cid}"
    elif DatabaseOption() == 'h':
        pass
    response = requests.delete(flask_url)
    return response

def Put_Client(cid, fname, lname, age, memberyear):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/client/{cid}"
    elif DatabaseOption() == 'h':
        pass
    data = {'fname': fname, 'lname': lname, 'age': age, 'memberyear': memberyear}
    response = requests.put(flask_url, json=data)
    return response
"""
-----------------------------------------------------------------------------------------------------------------------
Region Employee
-----------------------------------------------------------------------------------------------------------------------
"""

def Check_Employee(eid):
    flask_url = f"http://127.0.0.1:5000/db-beasts/employee/{eid}"
    response = requests.get(flask_url)
    return response







"""
-----------------------------------------------------------------------------------------------------------------------
Region Hotel
-----------------------------------------------------------------------------------------------------------------------
"""


def Post_Hotel(chid, hname, hcity):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/hotel"
    elif DatabaseOption() == 'h':
        pass
    data = {'chid': chid, 'hname': hname, 'hcity': hcity}
    response = requests.post(flask_url, json=data)
    return response


def Delete_Hotel(hid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}"
    elif DatabaseOption() == 'h':
        pass
    response = requests.delete(flask_url)
    return response


def Put_Hotel(hid, chid, hname, hcity):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}"
    elif DatabaseOption() == 'h':
        pass
    data = {'chid': chid, 'hname': hname, 'hcity': hcity}
    response = requests.put(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Login
-----------------------------------------------------------------------------------------------------------------------
"""






"""
-----------------------------------------------------------------------------------------------------------------------
Region Reserve
-----------------------------------------------------------------------------------------------------------------------
"""
def Post_Reserve(eid, rid, guests, startdate, enddate, clid, payment):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/reserve"
    elif DatabaseOption() == 'h':
        pass
    data = {'eid': eid, 'rid': rid, 'guests': guests, 'startdate': startdate, 'enddate': enddate, 'clid': clid, 'payment': payment}
    response = requests.post(flask_url, json=data)
    return response

def Delete_Reserve(rid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/reserve/{rid}"
    elif DatabaseOption() == 'h':
        pass
    response = requests.delete(flask_url)
    return response

def Put_Reserve(eid,reid,rid,guests,startdate,enddate,clid,payment):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/reserve/{reid}"
    elif DatabaseOption() == 'h':
        pass
    data = {'eid': eid, 'rid': rid, 'guests': guests, 'startdate': startdate, 'enddate': enddate, 'clid': clid, 'payment': payment}
    response = requests.put(flask_url, json=data)
    return response

"""
-----------------------------------------------------------------------------------------------------------------------
Region Room
-----------------------------------------------------------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------------------------------------------------------
Region Roomdescription
-----------------------------------------------------------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------------------------------------------------------
Region Roomunavailable
-----------------------------------------------------------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------------------------------------------------------
Region Globales
-----------------------------------------------------------------------------------------------------------------------
"""


# ###################### /most/revenue ##########################
def see_mostrevenue(id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/most/revenue"
    elif DatabaseOption() == 'h':
        pass
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


# ###################### /paymentmethod ##########################
def see_paymentmethod(id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/paymentmethod"
    elif DatabaseOption() == 'h':
        pass
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Locales
-----------------------------------------------------------------------------------------------------------------------
"""


# ###################### roomtype ##########################
def see_roomtype(hid, id):
    flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}/roomtype"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response
