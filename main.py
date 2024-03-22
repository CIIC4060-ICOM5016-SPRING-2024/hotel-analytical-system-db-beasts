from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# apply CORS
CORS(app)

"""
-----------------------------------------------------------------------------------------------------------------------
"""


@app.route('/', methods=['GET'])
def greeting():
    return 'Hello, this is the hotel-analytical-system-db-beasts app'


""""
-----------------------------------------------------------------------------------------------------------------------
GLOBAL STATISTICS
-----------------------------------------------------------------------------------------------------------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/revenue',  # Top 3 chains with the highest total revenue.
           methods=['POST'])
def most_revenue():
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/paymentmethod',  # Total reservation percentage by payment method.
           methods=['POST'])
def paymentmethod():
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/least/rooms',  # Top 3 chain with the least rooms.
           methods=['POST'])
def least_rooms():
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/capacity',  # Top 5 hotels with the most capacity.
           methods=['POST'])
def most_capacity():
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/reservation',  # Top 10% hotels that had the most reservations.
           methods=['POST'])
def most_reservation():
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/profitmonth',  # Top 3 month with the most reservation by chain.
           methods=['POST'])
def most_profitmonth():
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
CHAINS
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/chains',
           methods=['GET', 'POST'])
def chains():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/chains/<int:chains_id>',
           methods=['GET', 'PUT', 'DELETE'])
def chainsid(chains_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
HOTEL
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel',
           methods=['GET', 'POST'])
def hotel():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>',
           methods=['GET', 'PUT', 'DELETE'])
def hotelid(hotel_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------
LOCAL STATISTICS
-----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>/handicaproom',
           methods=['POST'])  # Top 5 handicap rooms that were reserve the most.
def handicaproom(hotel_id):
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>/leastreserve',
           methods=['POST'])  # Top 3 rooms that were the least time unavailable.
def leastreserve(hotel_id):
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>/mostcreditcard',
           methods=['POST'])  # Top 5 clients under 30 that made the most reservation with a credit card.
def mostcreditcard(hotel_id):
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>/highestpaid',
           methods=['POST'])  # Top 3 highest paid regular employees.
def highestpaid(hotel_id):
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>/mostdiscount',
           methods=['POST'])  # Top 5 clients that received the most discounts.
def mostdiscount(hotel_id):
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>/roomtype',
           methods=['POST'])  # Total reservation by room type.
def roomtype(hotel_id):
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/hotel/<int:hotel_id>/leastguests',
           methods=['POST'])  # Top 3 rooms that were reserved that had the least guest-to-capacity ratio.
def leastguests(hotel_id):
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
EMPLOYEE
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/employee',
           methods=['GET', 'POST'])
def employee():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/employee/<int:employee_id>',
           methods=['GET', 'PUT', 'DELETE'])
def employeeid(employee_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
LOGIN
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/login',
           methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/login/<int:login_id>',
           methods=['GET', 'PUT', 'DELETE'])
def loginid(login_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
ROOM
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/room',
           methods=['GET', 'POST'])
def room():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/room/<int:room_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomid(room_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
ROOM DESCRIPTION
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/roomdescription',
           methods=['GET', 'POST'])
def roomdescription():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/roomdescription/<int:roomdescription_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomdescriptionid(roomdescription_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
ROOM UNAVAILABLE
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/roomunavailable',
           methods=['GET', 'POST'])
def roomunavailable():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/roomunavailable/<int:roomunavailable_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomunavailableid(roomunavailable_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
RESERVE
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/reserve',
           methods=['GET', 'POST'])
def reserve():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/reserve/<int:reserve_id>',
           methods=['GET', 'PUT', 'DELETE'])
def reserveid(reserve_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


""""
-----------------------------------------------------------------------------------------------------------------------
CLIENT
-----------------------------------------------------------------------------------------------------------------------
"""

""""
----------------
CRUD OPERATIONS
----------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/client',
           methods=['GET', 'POST'])
def client():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/client/<int:client_id>',
           methods=['GET', 'PUT', 'DELETE'])
def clientid(client_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
"""

if __name__ == '__main__':
    app.run(debug=True)
