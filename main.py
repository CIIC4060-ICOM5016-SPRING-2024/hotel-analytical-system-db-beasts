from flask import Flask, request, jsonify
from flask_cors import CORS

# Controller Handler Imports
from controller_handler.chains import Chains_Controller_Handler
from controller_handler.employee import Employee_Controller_Handler
from controller_handler.login import Login_Controller_Handler
from controller_handler.room import Room_Controller_Handler
from controller_handler.roomdescription import RoomDescription_Controller_Handler

app = Flask(__name__)

# apply CORS
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
           '/most/revenue',  # Top 3 chains with the highest total revenue.
           methods=['POST'])
def most_revenue():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/paymentmethod',  # Total reservation percentage by payment method.
           methods=['POST'])
def paymentmethod():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/least/rooms',  # Top 3 chain with the least rooms.
           methods=['POST'])
def least_rooms():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/capacity',  # Top 5 hotels with the most capacity.
           methods=['POST'])
def most_capacity():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/reservation',  # Top 10% hotels that had the most reservations.
           methods=['POST'])
def most_reservation():  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/most/profitmonth',  # Top 3 month with the most reservation by chain.
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
def chainid(chain_id):  # TODO
    if request.method == 'GET':
        return Chains_Controller_Handler().Get_Chain(chain_id)
    elif request.method == 'PUT':
        chain_data = request.json
        return Chains_Controller_Handler().Put_Chain(chain_id, chain_data)
    elif request.method == 'DELETE':  # TODO
        # return Chains_Controller_Handler().Delete_Chain(chain_id)
        return jsonify("In Process")
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
def hotel():  # TODO
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>',
           methods=['GET', 'PUT', 'DELETE'])
def hotelid(hotel_id):  # TODO
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify("Not supported"), 405


"""
-------------------
* LOCAL STATISTICS
-------------------
"""


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/handicaproom',  # Top 5 handicap rooms that were reserve the most.
           methods=['POST'])
def handicaproom(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/leastreserve',  # Top 3 rooms that were the least time unavailable.
           methods=['POST'])
def leastreserve(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/mostcreditcard',  # Top 5 clients under 30 that
                                                    # made the most reservation with a credit card.
           methods=['POST'])
def mostcreditcard(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/highestpaid',  # Top 3 highest paid regular employees.
           methods=['POST'])
def highestpaid(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/mostdiscount',  # Top 5 clients that received the most discounts.
           methods=['POST'])
def mostdiscount(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/roomtype',  # Total reservation by room type.
           methods=['POST'])
def roomtype(hotel_id):  # TODO
    if request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/hotel/<int:hotel_id>/leastguests',  # Top 3 rooms that were reserved
                                                 # that had the least guest-to-capacity ratio.
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
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/employee/<int:employee_id>',
           methods=['GET', 'PUT', 'DELETE'])
def employeeid(employee_id):  # TODO
    if request.method == 'GET':
        return Employee_Controller_Handler().Get_Employee(employee_id)
    elif request.method == 'PUT':  # TODO
        pass
    elif request.method == 'DELETE':  # TODO
        pass
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
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/login/<int:login_id>',
           methods=['GET', 'PUT', 'DELETE'])
def loginid(login_id):  # TODO
    if request.method == 'GET':
        return Login_Controller_Handler().Get_Login(login_id)
    elif request.method == 'PUT':  # TODO
        pass
    elif request.method == 'DELETE':  # TODO
        pass
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
def room():  # TODO
    if request.method == 'GET':
        return Room_Controller_Handler().Get_All_Rooms()
    elif request.method == 'POST':  # TODO
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/room/<int:room_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomid(room_id):  # TODO
    if request.method == 'GET':
        return Room_Controller_Handler().Get_Room(room_id)
    elif request.method == 'PUT':  # TODO
        pass
    elif request.method == 'DELETE':  # TODO
        pass
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
def roomdescription():  # TODO
    if request.method == 'GET':
        return RoomDescription_Controller_Handler().Get_All_RoomDescriptions()
    elif request.method == 'POST':  # TODO
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/roomdescription/<int:roomdescription_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomdescriptionid(roomdescription_id):  # TODO
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
def roomunavailable():  # TODO
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/roomunavailable/<int:roomunavailable_id>',
           methods=['GET', 'PUT', 'DELETE'])
def roomunavailableid(roomunavailable_id):  # TODO
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
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/reserve/<int:reserve_id>',
           methods=['GET', 'PUT', 'DELETE'])
def reserveid(reserve_id):  # TODO
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
        pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify("Not supported"), 405


@app.route('/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts'
           '/client/<int:client_id>',
           methods=['GET', 'PUT', 'DELETE'])
def clientid(client_id):  # TODO
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
