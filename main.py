# ** Flask Import
from flask import Flask, request, jsonify
from flask_cors import CORS

# ** Controller Handler Imports
from controller_handler.chains import Chains_Controller_Handler
from controller_handler.employee import Employee_Controller_Handler
from controller_handler.login import Login_Controller_Handler
from controller_handler.room import Room_Controller_Handler
from controller_handler.roomdescription import RoomDescription_Controller_Handler
from controller_handler.roomunavailable import RoomUnavailable_Controller_Handler
from controller_handler.reserve import Reserve_Controller_Handler
from controller_handler.client import Client_Controller_Handler
from controller_handler.hotel import Hotel_Controller_Handler
from controller_handler.LocalStatistics import LocalStatistics_Controller_Handler
from controller_handler.GlobalStatistics import GlobalStatistics_Controller_Handler

app = Flask(__name__)

# ** apply CORS
CORS(app)

"""
-----------------------------------------------------------------------------------------------------------------------
"""


@app.route('/', methods=['GET'])
def greeting():
    return (''
            '<div '
            'style="text-align:center; '
            '       font-size: 50px;"'
            '>Hello, this is the hotel-analytical-system-db-beasts app'
            '</div>'
            )


"""
-----------------------------------------------------------------------------------------------------------------------
Region GLOBAL STATISTICS
-----------------------------------------------------------------------------------------------------------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/revenue',  # ** Top 3 chains with the highest total revenue.
           methods=['POST'])
def most_revenue():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/paymentmethod',  # ** Total reservation percentage by payment method.
           methods=['POST'])
def paymentmethod():
    if request.method == 'POST':
        data = request.json
        return GlobalStatistics_Controller_Handler().Get_post_PaymentMethod(data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/least/rooms',  # ** Top 3 chain with the least rooms.
           methods=['POST'])
def least_rooms():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/capacity',  # ** Top 5 hotels with the most capacity.
           methods=['POST'])
def most_capacity():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/reservation',  # ** Top 10% hotels that had the most reservations.
           methods=['POST'])
def most_reservation():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/profitmonth',  # ** Top 3 month with the most reservation by chain.
           methods=['POST'])
def most_profitmonth():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region CHAINS
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/chains',
           methods=['GET', 'POST'])
def chains():
    if request.method == 'GET':
        return Chains_Controller_Handler().Get_All_Chains()
    elif request.method == 'POST':
        chain_data = request.json
        return Chains_Controller_Handler().Post_Chain(chain_data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/chains/<int:chain_id>',
           methods=['GET', 'PUT', 'DELETE'])
def chainid(chain_id):
    if request.method == 'GET':
        return Chains_Controller_Handler().Get_Chain(chain_id)
    elif request.method == 'PUT':
        chain_data = request.json
        return Chains_Controller_Handler().Put_Chain(chain_id, chain_data)
    elif request.method == 'DELETE':
        return Chains_Controller_Handler().Delete_Chain(chain_id)
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region HOTEL
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel',
           methods=['GET', 'POST'])
def hotel():
    if request.method == 'GET':
        return Hotel_Controller_Handler().Get_All_Hotels()
    elif request.method == 'POST':
        data = request.json
        return Hotel_Controller_Handler().Post_Hotel(data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>',
           methods=['GET', 'PUT', 'DELETE'])
def hotelid(hotel_id):
    if request.method == 'GET':
        return Hotel_Controller_Handler().Get_Hotel(hotel_id)
    elif request.method == 'PUT':
        data = request.json
        return Hotel_Controller_Handler().Put_Hotel(hotel_id, data)
    elif request.method == 'DELETE':
        return Hotel_Controller_Handler().Delete_Hotel(hotel_id)
    else:
        return jsonify("Not supported"), 405


"""
-------------------
* LOCAL STATISTICS
-------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/handicaproom',  # ** Top 5 handicap rooms that were reserve the most.
           methods=['POST'])
def handicaproom(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/leastreserve',  # ** Top 3 rooms that were the least time unavailable.
           methods=['POST'])
def leastreserve(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/mostcreditcard',
           # ** Top 5 clients under 30 that
           # ** made the most reservation with a credit card.
           methods=['POST'])
def mostcreditcard(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/highestpaid',  # ** Top 3 highest paid regular employees.
           methods=['POST'])
def highestpaid(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/mostdiscount',  # ** Top 5 clients that received the most discounts.
           methods=['POST'])
def mostdiscount(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/roomtype',  # ** Total reservation by room type.
           methods=['POST'])
def roomtype(hotel_id):
    if request.method == 'POST':
        employee_id = request.json
        return (LocalStatistics_Controller_Handler()
                .Get_post_RoomType(hotel_id, employee_id))
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/leastguests',
           # ** Top 3 rooms that were reserved
           # ** that had the least guest-to-capacity ratio.
           methods=['POST'])
def leastguests(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region EMPLOYEE
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/employee',
           methods=['GET', 'POST'])
def employee():  # TODO
    if request.method == 'GET':
        return Employee_Controller_Handler().Get_All_Employees()
    elif request.method == 'POST':  # TODO
        data = request.json
        return Employee_Controller_Handler().Post_Employee(data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/employee/<int:employee_id>',
           methods=['GET', 'PUT', 'DELETE'])
def employeeid(employee_id):  # TODO
    if request.method == 'GET':
        return Employee_Controller_Handler().Get_Employee(employee_id)
    elif request.method == 'PUT':  # TODO
        data = request.json
        return Employee_Controller_Handler().Put_Employee(employee_id, data)
    elif request.method == 'DELETE':  # TODO
        return Employee_Controller_Handler().Delete_employee(employee_id)
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region LOGIN
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/login',
           methods=['GET', 'POST'])
def login():  # TODO
    if request.method == 'GET':
        return Login_Controller_Handler().Get_All_Logins()
    elif request.method == 'POST':  # TODO
        data = request.json
        return Login_Controller_Handler().Post_Login(data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/login/<int:login_id>',
           methods=['GET', 'PUT', 'DELETE'])
def loginid(login_id):  # TODO
    if request.method == 'GET':
        return Login_Controller_Handler().Get_Login(login_id)
    elif request.method == 'PUT':  # TODO
        data = request.json
        return Login_Controller_Handler().Put_Login(login_id, data)
    elif request.method == 'DELETE':  # TODO
        return Login_Controller_Handler().Delete_Login(login_id)
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region ROOM
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/room',
           methods=['GET', 'POST'])
def room():
    if request.method == 'GET':
        return Room_Controller_Handler().Get_All_Rooms()
    elif request.method == 'POST':
        data = request.json
        return Room_Controller_Handler().Post_Room(data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/room/<int:room_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomid(room_id):
    if request.method == 'GET':
        return Room_Controller_Handler().Get_Room(room_id)
    elif request.method == 'PUT':
        data = request.json
        return Room_Controller_Handler().Put_Room(room_id, data)
    elif request.method == 'DELETE':
        return Room_Controller_Handler().Delete_Room(room_id)
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region ROOM DESCRIPTION
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/roomdescription',
           methods=['GET', 'POST'])
def roomdescription():
    if request.method == 'GET':
        return RoomDescription_Controller_Handler().Get_All_RoomDescriptions()
    elif request.method == 'POST':
        data = request.json
        return RoomDescription_Controller_Handler().Post_RoomDescription(data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/roomdescription/<int:roomdescription_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomdescriptionid(roomdescription_id):
    if request.method == 'GET':
        return RoomDescription_Controller_Handler().Get_RoomDescription(roomdescription_id)
    elif request.method == 'PUT':
        data = request.json
        return RoomDescription_Controller_Handler().Put_RoomDescription(roomdescription_id, data)
    elif request.method == 'DELETE':
        return RoomDescription_Controller_Handler().Delete_RoomDescription(roomdescription_id)
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region ROOM UNAVAILABLE
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/roomunavailable',
           methods=['GET', 'POST'])
def roomunavailable():
    if request.method == 'GET':
        return RoomUnavailable_Controller_Handler().Get_All_RoomsUnavailable()
    elif request.method == 'POST':
        data = request.json
        return RoomUnavailable_Controller_Handler().Post_RoomUnavailable(data)
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/roomunavailable/<int:roomunavailable_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomunavailableid(roomunavailable_id):  # TODO
    if request.method == 'GET':
        return RoomUnavailable_Controller_Handler().Get_RoomUnavailable(roomunavailable_id)
    elif request.method == 'PUT':  # TODO
        data = request.json
        return RoomUnavailable_Controller_Handler().Put_RoomUnavailable(roomunavailable_id, data)
    elif request.method == 'DELETE':
        data = request.json
        return RoomUnavailable_Controller_Handler().Delete_RoomUnavailable(roomunavailable_id, data)
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region RESERVE
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/reserve',
           methods=['GET', 'POST'])
def reserve():  # TODO
    if request.method == 'GET':
        return Reserve_Controller_Handler().Get_All_Reserves()
    elif request.method == 'POST':  # TODO
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/reserve/<int:reserve_id>',
           methods=['GET', 'PUT', 'DELETE'])
def reserveid(reserve_id):  # TODO
    if request.method == 'GET':
        return Reserve_Controller_Handler().Get_Reserve(reserve_id)
    elif request.method == 'PUT':  # TODO
        pass
    elif request.method == 'DELETE':  # TODO
        pass
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
Region CLIENT
-----------------------------------------------------------------------------------------------------------------------
"""

"""
------------------
* CRUD OPERATIONS
------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/client',
           methods=['GET', 'POST'])
def client():  # TODO
    if request.method == 'GET':
        return Client_Controller_Handler().Get_All_Clients()
    elif request.method == 'POST':  # TODO
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/client/<int:client_id>',
           methods=['GET', 'PUT', 'DELETE'])
def clientid(client_id):  # TODO
    if request.method == 'GET':
        return Client_Controller_Handler().Get_Client(client_id)
    elif request.method == 'PUT':  # TODO
        pass
    elif request.method == 'DELETE':  # TODO
        pass
    else:
        return jsonify("Not supported"), 405


"""
-----------------------------------------------------------------------------------------------------------------------
"""

if __name__ == '__main__':
    app.run(debug=True)
