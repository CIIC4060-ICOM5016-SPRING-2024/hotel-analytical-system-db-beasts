# ** Importing necessary modules
from model_dao.room import ROOM_Model_Dao
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

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all rooms
    def Get_All_Rooms(self):
        dao = ROOM_Model_Dao()
        rooms = dao.Get_All_Rooms()
        result = []
        for room in rooms:
            result.append(self.Room_Dict(room))
        return jsonify(Rooms=result)

    # ** Method to retrieve a specific room by its ID
    def Get_Room(self, room_id):
        dao = ROOM_Model_Dao()
        room = dao.Get_Room(room_id)
        if room:
            result = self.Room_Dict(room)
            return jsonify(Room=result)
        return jsonify(Error="Not Found"), 404
