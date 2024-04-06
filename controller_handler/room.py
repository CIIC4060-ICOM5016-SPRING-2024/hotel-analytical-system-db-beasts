# ** Importing necessary modules
from model_dao.room import Room_Model_Dao
from model_dao.hotel import Hotel_Model_Dao
from model_dao.roomdescription import RoomDescription_Model_Dao

from flask import jsonify


# ** Class for handling HTTP requests related to room
class Room_Controller_Handler:
    # ** Method to create a dictionary representation of room data
    def Room_Dict(self, r):
        room_dict = {
            'rid': r[0],
            'hid': r[1],
            'rdid': r[2],
            'rprice': r[3]
        }
        return room_dict

    # ** Method to build a dictionary representation of room data
    def Room_Build(self, rid, hid, rdid, rprice):
        room_build = {
            'rid': rid,
            'hid': hid,
            'rdid': rdid,
            'rprice': rprice
        }
        return room_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all rooms
    def Get_All_Rooms(self):
        dao = Room_Model_Dao()
        rooms = dao.Get_All_Rooms()
        result = []
        for room in rooms:
            result.append(self.Room_Dict(room))
        return jsonify(Rooms=result)

    # ** Method to retrieve a specific room by its ID
    def Get_Room(self, room_id):
        dao = Room_Model_Dao()
        room = dao.Get_Room(room_id)
        if room:
            result = self.Room_Dict(room)
            return jsonify(Room=result)
        return jsonify(Error="Not Found"), 404

    # ** Method to add a new room
    def Post_Room(self, room_data):
        if len(room_data) != 3:
            return jsonify(Error="Invalid Data"), 400

        daoH = Hotel_Model_Dao()
        daoR = Room_Model_Dao()
        daoRD = RoomDescription_Model_Dao()

        hid = room_data['hid']
        if not daoH.Get_Hotel(hid):
            return jsonify(Error="Hotel Not Found"), 404

        rdid = room_data['rdid']
        if not daoRD.Get_RoomDescription(rdid):
            return jsonify(Error="Room Description Not Found"), 404

        rprice = room_data['rprice']

        if rprice >= 0:
            room_id = daoR.Post_Room(hid, rdid, rprice)
            result = self.Room_Build(room_id, hid, rdid, rprice)
            return jsonify(Room=result), 201
        else:
            return jsonify(Error="Unexpected attribute values."), 400

    # ** Method to update an existing room
    def Put_Room(self, rid, room_data):
        if len(room_data) != 3:
            return jsonify(Error="Invalid Data"), 400

        daoH = Hotel_Model_Dao()
        daoRD = RoomDescription_Model_Dao()
        daoR = Room_Model_Dao()

        if not daoR.Get_Room(rid):
            return jsonify(Error="Room Not Found"), 404

        hid = room_data['hid']
        if not daoH.Get_Hotel(hid):
            return jsonify(Error="Hotel Not Found"), 404

        rdid = room_data['rdid']
        if not daoRD.Get_RoomDescription(rdid):
            return jsonify(Error="Room Description Not Found"), 404

        rprice = room_data['rprice']

        if rprice >= 0:
            daoR = Room_Model_Dao()
            daoR.Put_Room(rid, hid, rdid, rprice)
            result = self.Room_Build(rid, hid, rdid, rprice)
            return jsonify(Room=result), 200
        else:
            return jsonify(Error="Unexpected attribute values."), 400

    # ** Method to delete an existing room
    def Delete_Room(self, rid):
        daoR = Room_Model_Dao()
        room = daoR.Get_Room(rid)
        if not room:
            return jsonify(Error="Room Not Found"), 404
        daoR1 = Room_Model_Dao()
        result = daoR1.Delete_Room(rid)
        if result == "Error deleting":
            return jsonify(Error="Room is referenced"), 400
        elif result:
            return jsonify(OK="Room Deleted Successfully"), 200
        else:
            return jsonify(Error="Delete Failed"), 500
