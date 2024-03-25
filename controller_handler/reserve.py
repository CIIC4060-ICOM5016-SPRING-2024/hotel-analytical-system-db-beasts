# Importing necessary modules
from model_dao.reserve import Reserve_Model_Dao
from flask import jsonify


# Class for handling HTTP requests related to reserve
class Reserve_Controller_Handler:
    # Method to create a dictionary representation of reserve data
    def Reserve_Dict(self, r):
        reserve_dict = {
            'reid': r[0],
            'ruid': r[1],
            'clid': r[2],
            'total_cost': r[3],
            'payment': r[4],
            'guests': r[5]
        }
        return reserve_dict

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to retrieve all reserves
    def Get_All_Reserves(self):
        data = Reserve_Model_Dao()
        reserves = data.Get_All_Reserves()
        result = []
        for reserve in reserves:
            result.append(self.Reserve_Dict(reserve))
        return jsonify(reserves=result)

    def Get_Reserve(self, reserve_id):
        dao = Reserve_Model_Dao()
        reserve = dao.Get_Reserve(reserve_id)
        if reserve:
            result = self.Reserve_Dict(reserve)
            return jsonify(reserve=result)
        return jsonify("Not Found"), 404
