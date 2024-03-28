# ** Importing necessary modules
from model_dao.reserve import Reserve_Model_Dao
from flask import jsonify


# ** Class for handling HTTP requests related to reserve
class Reserve_Controller_Handler:
    # ** Method to create a dictionary representation of reserve data
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
    
    def Reserve_Build(self, reid, ruid, clid, total_cost, payment, guests):
        reserve_build = {
            'reid': reid,
            'ruid': ruid,
            'clid': clid,
            'total_cost': total_cost,
            'payment': payment,
            'guests': guests
        }
        return reserve_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all reserves
    def Get_All_Reserves(self):
        dao = Reserve_Model_Dao()
        reserves = dao.Get_All_Reserves()
        result = []
        for reserve in reserves:
            result.append(self.Reserve_Dict(reserve))
        return jsonify(reserves=result)

    # ** Method to retrieve a specific reserve by its ID
    def Get_Reserve(self, reserve_id):
        dao = Reserve_Model_Dao()
        reserve = dao.Get_Reserve(reserve_id)
        if reserve:
            result = self.Reserve_Dict(reserve)
            return jsonify(reserve=result)
        return jsonify("Not Found"), 404
    
    def Post_Reserve(self, reserve_data):
        if len(reserve_data) != 6:
            return jsonify(Error="Invalid Data"), 400
        dao = Reserve_Model_Dao()
        
        reid = reserve_data['reid']
        ruid = reserve_data['ruid']
        clid = reserve_data['clid']
        total_cost = reserve_data['total_cost']
        payment = reserve_data['payment']
        guests = reserve_data['guests']
        #Check for none values
        if any(v is None for v in (reid, ruid, clid, total_cost, payment, guests)):
            return jsonify("Unexpected attribute values."), 400
        else:
            reserve_id = dao.Post_Reserve(reid, ruid, clid, total_cost, payment, guests)
            result = self.Reserve_Build(reserve_id, ruid, clid, total_cost, payment, guests) 
            return jsonify(reserve=result),201
        
    def Put_Reserve(self,reserve_id, reserve_data):
        if len(reserve_data) != 5:
            return jsonify(Error="Invalid Data"), 400
        # ** Models/Daos to use
        dao = Reserve_Model_Dao()
        
        # ** Data received
        ruid = reserve_data['ruid']
        clid = reserve_data['clid']
        total_cost = reserve_data['total_cost']
        payment = reserve_data['payment']
        guests = reserve_data['guests']
        # ** Search chid if exists
        if (reserve_id or reserve_id == 0) and ruid and clid and total_cost and payment and guests:
            reserve = dao.Put_Reserve(ruid, clid, total_cost, payment, guests,reserve_id)
            result = self.Reserve_Build(reserve_id, ruid, clid, total_cost, payment, guests)
            if reserve:
                return jsonify(reserve=result), 200
            else:
                return jsonify("Reserve Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400
    
    
    def Delete_Reserve(self, reserve_id):
        if reserve_id or reserve_id == 0:
            dao = Reserve_Model_Dao()
            result = dao.Delete_Reserve(reserve_id)
            if result == 'Error deleting':    
                return jsonify("Reserve is referenced"), 200
            elif result:
                return jsonify("Deleted"), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Error deleting"), 400