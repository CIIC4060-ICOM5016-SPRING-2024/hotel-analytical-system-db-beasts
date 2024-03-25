# Importing necessary modules
from model_dao.roomunavailable import RoomUnavailable_Model_Dao
from flask import jsonify


# Class for handling HTTP requests related to RoomUnavailable
class RoomUnavailable_Controller_Handler:
    # Method to create a dictionary representation of RoomUnavailable data
    def RoomUnavailable_Dict(self, r):
        roomunavailable_dict = {
            'ruid': r[0],
            'rid': r[1],
            'startdate': r[2],
            'enddate': r[3],
        }
        return roomunavailable_dict

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to retrieve all RoomsUnavailable
    def Get_All_RoomsUnavailable(self):
        dao = RoomUnavailable_Model_Dao()
        roomsunavailable = dao.Get_All_RoomsUnavailable()
        result = []
        for roomunavailable in roomsunavailable:
            result.append(self.RoomUnavailable_Dict(roomunavailable))
        return jsonify(roomsunavailable=result)
