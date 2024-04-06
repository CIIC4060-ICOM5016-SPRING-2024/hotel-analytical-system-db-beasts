# ** Importing necessary modules
from model_dao.hotel import Hotel_Model_Dao
from model_dao.chains import Chains_Model_Dao
from flask import jsonify


# ** Class for handling HTTP requests related to hotel
class Hotel_Controller_Handler:

    # ** Method to create a dictionary representation of Hotel data
    def Hotel_Dict(self, r):
        hotel_dict = {
            'hid': r[0],
            'chid': r[1],
            'hname': r[2],
            'hcity': r[3]
        }
        return hotel_dict

    # ** Method to build a dictionary representation of hotel data
    def Hotel_Build(self, hid, chid, hname, hcity):
        hotel_build = {
            'hid': hid,
            'chid': chid,
            'hname': hname,
            'hcity': hcity
        }
        return hotel_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all hotels
    def Get_All_Hotels(self):
        dao = Hotel_Model_Dao()
        hotels = dao.Get_All_Hotels()
        result = []
        for hotel in hotels:
            result.append(self.Hotel_Dict(hotel))
        return jsonify(Hotels=result)

    # ** Method to retrieve a specific hotel by its ID
    def Get_Hotel(self, hotel_id):
        dao = Hotel_Model_Dao()
        hotel = dao.Get_Hotel(hotel_id)
        if hotel:
            result = self.Hotel_Dict(hotel)
            return jsonify(Hotel=result)
        return jsonify(Error="Not Found"), 404

    # ** Method to add a new hotel
    def Post_Hotel(self, hotel_data):
        if len(hotel_data) != 3:
            return jsonify(Error="Invalid Data"), 400
        # ** Models/Daos to use
        daoc = Chains_Model_Dao()
        daoh = Hotel_Model_Dao()
        # ** Data received
        chid = hotel_data['chid']
        hname = hotel_data['hname']
        hcity = hotel_data['hcity']
        # ** Search chid if exists
        if not daoc.Get_Chain(chid):
            return jsonify(Error="Chain not found"), 404
        if hname and hcity:
            hotel_id = daoh.Post_Hotel(chid, hname, hcity)
            result = self.Hotel_Build(hotel_id, chid, hname, hcity)
            return jsonify(Hotel=result), 201
        else:
            return jsonify(Error="Unexpected attribute values."), 400

    # ** Method to update an existing hotel
    def Put_Hotel(self, hid, hotel_data):
        if len(hotel_data) != 3:
            return jsonify(Error="Invalid Data"), 400
        # ** Models/Daos to use
        daoc = Chains_Model_Dao()
        daoh = Hotel_Model_Dao()
        # ** Data received
        chid = hotel_data['chid']
        hname = hotel_data['hname']
        hcity = hotel_data['hcity']
        # ** Search chid if exists
        if not daoc.Get_Chain(chid):
            return jsonify(Error="Chain not found"), 404
        if (hid or hid == 0) and hname and hcity:
            hotel = daoh.Put_Hotel(hid, chid, hname, hcity)
            result = self.Hotel_Build(hid, chid, hname, hcity)
            if hotel:
                return jsonify(Hotel=result), 200
            else:
                return jsonify(Error="Hotel not found"), 404
        else:
            return jsonify(Error="Unexpected attribute values."), 400

    # ** Method to delete an existing hotel
    def Delete_Hotel(self, hid):
        if hid or hid == 0:
            dao = Hotel_Model_Dao()
            result = dao.Delete_Hotel(hid)
            if result == "Error deleting":
                return jsonify(Error="Hotel is referenced"), 400
            elif result:
                return jsonify(OK="Deleted"), 200
            else:
                return jsonify(Error="Not Found"), 404
        else:
            return jsonify(Error="Error deleting"), 400
