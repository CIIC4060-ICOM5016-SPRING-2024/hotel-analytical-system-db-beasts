# Importing necessary modules
from model_dao.roomdescription import RoomDescription_Model_Dao
from flask import jsonify


# Class for handling HTTP requests related to RoomDescription
class RoomDescription_Controller_Handler:
    # Method to create a dictionary representation of RoomDescription data
    def RoomDescription_Dict(self, r):
        roomdescription_dict = {
            'rdid': r[0],
            'rname': r[1],
            'rtype': r[2],
            'capacity': r[3],
            'ishandicap': r[4]
        }
        return roomdescription_dict

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to retrieve all RoomDescriptions
    def Get_All_RoomDescriptions(self):
        dao = RoomDescription_Model_Dao()
        roomdescriptions = dao.Get_All_RoomDescriptions()
        result = []
        for roomdescription in roomdescriptions:
            result.append(self.RoomDescription_Dict(roomdescription))
        return jsonify(roomdescriptions=result)

    # Method to retrieve a specific RoomDescription by its ID
    def Get_RoomDescription(self, roomdescription_id):
        dao = RoomDescription_Model_Dao()
        roomdescription = dao.Get_RoomDescription(roomdescription_id)
        if roomdescription:
            result = self.RoomDescription_Dict(roomdescription)
            return jsonify(roomdescription=result)
        return jsonify("Not Found"), 404
