from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# apply CORS
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the hotel-analytical-system-db-beasts app'


""""
-----------------------------------------------------------------------------------------------------------------------
CHAINS
-----------------------------------------------------------------------------------------------------------------------
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
-----------------------------------------------------------------------------------------------------------------------
EMPLOYEE
-----------------------------------------------------------------------------------------------------------------------
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


if __name__ == '__main__':
    app.run(debug=True)
