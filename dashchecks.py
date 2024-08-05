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
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/logincred"
    elif DatabaseOption() == 'h':
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/logincred"
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
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/login"
    data = {'eid': eid, 'username': username, 'password': password}
    response = requests.post(flask_url, json=data)
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
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/chains"
    data = {'cname': cname, 'fallmkup': fallmkup, 'springmkup': springmkup, 'summermkup': summermkup,
            'wintermkup': wintermkup}
    response = requests.post(flask_url, json=data)
    return response


def Delete_Chain(chid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/chains/{chid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/chains/{chid}"
    response = requests.delete(flask_url)
    return response


def Put_Chain(chid, cname, fallmkup, springmkup, summermkup, wintermkup):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/chains/{chid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/chains/{chid}"
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
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/client"
    data = {'fname': fname, 'lname': lname, 'age': age, 'memberyear': memberyear}
    response = requests.post(flask_url, json=data)
    return response


def Delete_Client(cid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/client/{cid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/client/{cid}"
    response = requests.delete(flask_url)
    return response


def Put_Client(cid, fname, lname, age, memberyear):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/client/{cid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/client/{cid}"
    data = {'fname': fname, 'lname': lname, 'age': age, 'memberyear': memberyear}
    response = requests.put(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Employee
-----------------------------------------------------------------------------------------------------------------------
"""


def Post_Employee(hid, position, salary, fname, lname, age, username, password):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/employee"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/employee"
    data = {
        'hid': hid,
        'position': position,
        'salary': salary,
        'fname': fname,
        'lname': lname,
        'age': age,
        'username': username,
        'password': password
    }
    response = requests.post(flask_url, json=data)
    return response


def Delete_Employee(eid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/employee/{eid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/employee/{eid}"
    response = requests.delete(flask_url)
    return response


def Check_Employeee(eid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/employee/{eid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/employee/{eid}"
    response = requests.get(flask_url)
    return response

def Put_Employee(eid, hid, position, salary, fname, lname, age):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/employee/{eid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/employee/{eid}"
    data = {
        'hid': hid,
        'position': position,
        'salary': salary,
        'fname': fname,
        'lname': lname,
        'age': age,
    }
    response = requests.put(flask_url, json=data)
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
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel"
    data = {'chid': chid, 'hname': hname, 'hcity': hcity}
    response = requests.post(flask_url, json=data)
    return response


def Delete_Hotel(hid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}"
    response = requests.delete(flask_url)
    return response


def Put_Hotel(hid, chid, hname, hcity):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}"
    data = {'chid': chid, 'hname': hname, 'hcity': hcity}
    response = requests.put(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Login
-----------------------------------------------------------------------------------------------------------------------
"""

def Delete_Login(lid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/login/{lid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/login/{lid}"
    response = requests.delete(flask_url)
    return response




def Put_Login(lid, username, password):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/login/{lid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/login/{lid}"
    data = {'username': username, 'password': password}
    response = requests.put(flask_url, json=data)
    return response

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
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/reserve"
    data = {'eid': eid, 'rid': rid, 'guests': guests, 'startdate': startdate, 'enddate': enddate, 'clid': clid,
            'payment': payment}
    response = requests.post(flask_url, json=data)
    return response


def Delete_Reserve(rid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/reserve/{rid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/reserve/{rid}"
    response = requests.delete(flask_url)
    return response


def Put_Reserve(eid, reid, rid, guests, startdate, enddate, clid, payment):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/reserve/{reid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/reserve/{reid}"
    data = {'eid': eid, 'rid': rid, 'guests': guests, 'startdate': startdate, 'enddate': enddate, 'clid': clid,
            'payment': payment}
    response = requests.put(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Room
-----------------------------------------------------------------------------------------------------------------------
"""


def Post_Room(hid, rdid, rprice):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/room"
    elif DatabaseOption() == 'h':
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/room"
    data = {'hid': hid, 'rdid': rdid, 'rprice': rprice}
    response = requests.post(flask_url, json=data)
    return response


def Delete_Room(rid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/room/{rid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/room/{rid}"
    response = requests.delete(flask_url)
    return response


def Put_Room(rid, hid, rdid, rprice):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/room/{rid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/room/{rid}"
    data = {'hid': hid, 'rdid': rdid, 'rprice': rprice}
    response = requests.put(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Roomdescription
-----------------------------------------------------------------------------------------------------------------------
"""


def Post_RoomDescription(capacity, ishandicap, rname, rtype):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/roomdescription"
    elif DatabaseOption() == 'h':
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/roomdescription"
    data = {'capacity': capacity, 'ishandicap': ishandicap, 'rname': rname, 'rtype': rtype}
    response = requests.post(flask_url, json=data)
    return response


def Delete_RoomDescription(rdid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/roomdescription/{rdid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/roomdescription/{rdid}"
    response = requests.delete(flask_url)
    return response


def Put_RoomDescription(rdid, capacity, ishandicap, rname, rtype):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/roomdescription/{rdid}"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/roomdescription/{rdid}"
    data = {'capacity': capacity, 'ishandicap': ishandicap, 'rname': rname, 'rtype': rtype}
    response = requests.put(flask_url, json=data)
    return response


"""
-----------------------------------------------------------------------------------------------------------------------
Region Roomunavailable
-----------------------------------------------------------------------------------------------------------------------
"""


def Post_RoomUnavailable(id, rid, startdate, enddate):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = 'http://127.0.0.1:5000/db-beasts/roomunavailable'
    elif DatabaseOption() == 'h':
        flask_url = 'https://db-beasts-7827ce232282.herokuapp.com/db-beasts/roomunavailable'
    data = {'eid': id, 'rid': rid, 'startdate': startdate, 'enddate': enddate}
    respond = requests.post(flask_url, json=data)
    return respond


def Delete_RoomUnavailable(id, ruid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f'http://127.0.0.1:5000/db-beasts/roomunavailable/{ruid}'
    elif DatabaseOption() == 'h':
        flask_url = f'https://db-beasts-7827ce232282.herokuapp.com/db-beasts/roomunavailable/{ruid}'
    data = {'eid': id}
    respond = requests.delete(flask_url, json=data)
    return respond


def Put_RoomUnavailable(id, ruid, rid, startdate, enddate):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f'http://127.0.0.1:5000/db-beasts/roomunavailable/{ruid}'
    elif DatabaseOption() == 'h':
        flask_url = f'https://db-beasts-7827ce232282.herokuapp.com/db-beasts/roomunavailable/{ruid}'
    data = {'eid': id, 'rid': rid, 'startdate': startdate, 'enddate': enddate}
    respond = requests.put(flask_url, json=data)
    return respond


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
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/most/revenue"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


# ###################### /paymentmethod ##########################
def see_paymentmethod(id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = "http://127.0.0.1:5000/db-beasts/paymentmethod"
    elif DatabaseOption() == 'h':
        flask_url = "https://db-beasts-7827ce232282.herokuapp.com/db-beasts/paymentmethod"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


def see_least_rooms_chains(id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts//least/rooms"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts//least/rooms"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


def see_most_capacity_per_chain(id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/most/capacity" 
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/most/capacity"
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
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}/roomtype"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}/roomtype"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


# ###################### mostcreditcard ##########################
def see_mostcreditcard(hid, id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}/mostcreditcard"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}/mostcreditcard"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


# ###################### leastguests ##########################
def see_leastguests(hid, id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}/leastguests"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}/leastguests"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


# ###################### handicaproom ##########################
def handicap_room(hid, eid):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}/handicaproom"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}/handicaproom"
    data = {'eid': eid}
    response = requests.post(flask_url, json=data)
    return response

############################ highest paid #####################################

def see_highest_paid(hid, id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}/highestpaid"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}/highestpaid"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response


######################### most discounts ######################################

def see_top_discount_clients(hid, id):
    flask_url = None
    if DatabaseOption() == 'd':
        flask_url = f"http://127.0.0.1:5000/db-beasts/hotel/{hid}/mostdiscount"
    elif DatabaseOption() == 'h':
        flask_url = f"https://db-beasts-7827ce232282.herokuapp.com/db-beasts/hotel/{hid}/mostdiscount"
    data = {'eid': id}
    response = requests.post(flask_url, json=data)
    return response