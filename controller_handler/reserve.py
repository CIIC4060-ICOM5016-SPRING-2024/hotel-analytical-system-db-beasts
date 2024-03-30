# ** Importing necessary modules
from model_dao.reserve import Reserve_Model_Dao
from model_dao.employee import Employee_Model_Dao
from model_dao.room import ROOM_Model_Dao
from model_dao.client import Client_Model_Dao
from model_dao.roomunavailable import RoomUnavailable_Model_Dao
from flask import jsonify
from datetime import datetime
from controller_handler.roomunavailable import RoomUnavailable_Controller_Handler


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
        # ** Checking if all data was entered.
        if len(reserve_data) != 8:
            return jsonify(Error="Invalid Data"), 400
        # ** Checking employee information
        eid = reserve_data['eid']
        daoEmployee = Employee_Model_Dao()
        employee = daoEmployee.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found."), 404
        if employee[5] != "Regular":
            return jsonify(Error="The employee position is not Regular"), 401
        # ** Checking room based on the hotel where the employee works
        rid = reserve_data['rid']
        daoRoom = ROOM_Model_Dao()
        room = daoRoom.Get_Room_Info(rid, employee[1])
        if not room:
            return jsonify(Error=f"Room not found in the hotel = {employee[1]}."), 404
        guests = reserve_data['guests']
        if room[3] < guests:
            return jsonify(Error=f"Insufficient capacity = {room[3]}")
        # ** Checking length of stay
        startdate = reserve_data['startdate']
        enddate = reserve_data['enddate']
        if enddate <= startdate:
            return jsonify(Error="End date must be greater than start date"), 400
        # ** Checking disponibility
        daoRU1 = RoomUnavailable_Model_Dao()
        not_disponibility = daoRU1.RoomUnavailable_Time(rid)
        startdate_date = datetime.strptime(startdate, '%Y-%m-%d').date()
        if not_disponibility[0] >= startdate_date:
            return jsonify(Error=f"Room is not available during the selected dates. "
                                 f"not_disponibility={not_disponibility[0]} vs "
                                 f"startdate={startdate}"), 400
        # ** Checking existence of the client
        clid = reserve_data['clid']
        daoClient = Client_Model_Dao()
        if not daoClient.Get_Client(clid):
            return jsonify(Error="Client not found."), 404

        total_cost = reserve_data['total_cost']
        payment = reserve_data['payment']

        # Check for none values
        if total_cost >= 0 and payment:
            # ** Creating new room unavailability for the indicated dates
            daoRU2 = RoomUnavailable_Model_Dao()
            ruid = daoRU2.Post_RoomUnavailable(rid, startdate, enddate)
            controller_handler_ruid = RoomUnavailable_Controller_Handler()
            roomunavailable_result = controller_handler_ruid.RoomUnavailable_Build(ruid, rid, startdate, enddate)
            if not ruid:
                return jsonify(Error="The room could not be separated."), 404
            # ** Creating reservation based on the new room unavailability
            daoRU = Reserve_Model_Dao()
            reserve_id = daoRU.Post_Reserve(ruid, clid, total_cost, payment, guests)
            reserve_result = self.Reserve_Build(reserve_id, ruid, clid, total_cost, payment, guests)
            return jsonify(reserve=reserve_result, roomunavailable=roomunavailable_result), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def Put_Reserve(self, reserve_id, reserve_data):
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
            reserve = dao.Put_Reserve(ruid, clid, total_cost, payment, guests, reserve_id)
            result = self.Reserve_Build(reserve_id, ruid, clid, total_cost, payment, guests)
            if reserve:
                return jsonify(reserve=result), 200
            else:
                return jsonify("Reserve Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400

    def Delete_Reserve(self, reserve_id):
        # Delete reserve
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
