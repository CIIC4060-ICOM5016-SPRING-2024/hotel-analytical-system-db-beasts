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

"""
-----------------------------------------------------------------------------------------------------------------------
Region Employee
-----------------------------------------------------------------------------------------------------------------------
"""

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
def see_mostrevenue():
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/most/revenue"
    elif DatabaseOption() == 'h':
        pass
    data = {'eid': 3}
    response = requests.post(flask_url, json=data)
    return response


# ######################      /paymentmethod ##########################
def see_paymentmethod():
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/paymentmethod"
    elif DatabaseOption() == 'h':
        pass
    data = {'eid': 3}
    response = requests.post(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Locales
-----------------------------------------------------------------------------------------------------------------------
"""
