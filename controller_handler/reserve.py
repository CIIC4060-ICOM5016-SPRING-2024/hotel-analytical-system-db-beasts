# ** Importing necessary modules
from flask import jsonify
from datetime import datetime

from model_dao.reserve import Reserve_Model_Dao
from model_dao.employee import Employee_Model_Dao
from model_dao.room import Room_Model_Dao
from model_dao.client import Client_Model_Dao
from model_dao.roomunavailable import RoomUnavailable_Model_Dao
from model_dao.roomdescription import RoomDescription_Model_Dao
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
        data = Reserve_Model_Dao()
        reserves = data.Get_All_Reserves()
        result = []
        for reserve in reserves:
            result.append(self.Reserve_Dict(reserve))
        return jsonify(Reserves=result)

    # ** Method to retrieve a specific reserve by its ID
    def Get_Reserve(self, reserve_id):
        dao = Reserve_Model_Dao()
        reserve = dao.Get_Reserve(reserve_id)
        if reserve:
            result = self.Reserve_Dict(reserve)
            return jsonify(Reserve=result)
        return jsonify(Error="Not Found"), 404

    def Post_Reserve(self, reserve_data):
        # ** Checking if all data was entered.
        if len(reserve_data) != 7:
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
        daoRoom = Room_Model_Dao()
        room = daoRoom.Get_Room_Info(rid, employee[1])
        if not room:
            return jsonify(Error=f"The room = {rid} was not found in the hotel = {employee[1]} "
                                 f"where the employee = {employee[0]} works."), 404
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
                                 f"not_disponibility = {not_disponibility[0]} vs "
                                 f"startdate = {startdate}"), 400
        # ** Checking existence of the client
        clid = reserve_data['clid']
        daoClient = Client_Model_Dao()
        if not daoClient.Get_Client(clid):
            return jsonify(Error="Client not found."), 404

        daoRE = Reserve_Model_Dao()
        total_cost_auto = daoRE.Get_Total_Cost(rid, clid, startdate, enddate)

        payment = reserve_data['payment']

        # ** Check for none values
        if payment:
            # ** Creating new room unavailability for the indicated dates
            daoRU2 = RoomUnavailable_Model_Dao()
            ruid = daoRU2.Post_RoomUnavailable(rid, startdate, enddate)
            controller_handler_ruid = RoomUnavailable_Controller_Handler()
            roomunavailable_result = controller_handler_ruid.RoomUnavailable_Build(ruid, rid, startdate, enddate)
            if not ruid:
                return jsonify(Error="The room could not be separated."), 404
            # ** Creating reservation based on the new room unavailability
            daoRU = Reserve_Model_Dao()
            reserve_id = daoRU.Post_Reserve(ruid, clid, total_cost_auto, payment, guests)
            reserve_result = self.Reserve_Build(reserve_id, ruid, clid, total_cost_auto, payment, guests)
            return jsonify(Reserve=reserve_result, RoomUnavailable=roomunavailable_result), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def Put_Reserve(self, reid, reserve_data):
        if len(reserve_data) != 7:
            return jsonify(Error="Invalid Data"), 400

        daoRe = Reserve_Model_Dao()
        reserve_info = daoRe.Get_Reserve(reid)
        if not reserve_info:
            return jsonify(Error="Reserve Not Found"), 404

        eid = reserve_data['eid']
        daoEmployee = Employee_Model_Dao()
        employee = daoEmployee.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found."), 404
        if employee[5] != "Regular":
            return jsonify(Error="The employee position is not Regular"), 401

        ruid = reserve_info[1]

        rid = reserve_data['rid']
        daoRo = Room_Model_Dao()
        room_info = daoRo.Get_Room_Info(rid, employee[1])
        if not room_info:
            return jsonify(Error=f"The room = {rid} was not found in the hotel = {employee[1]} "
                                 f"where the employee = {employee[0]} works."), 404

        rdid = room_info[2]
        daoRD = RoomDescription_Model_Dao()
        roomdescription_info = daoRD.Get_RoomDescription(rdid)

        guests = reserve_data['guests']
        if roomdescription_info[3] < guests:
            return jsonify(Error=f"Insufficient capacity = {roomdescription_info[3]}")

        startdate = reserve_data['startdate']
        enddate = reserve_data['enddate']
        if enddate <= startdate:
            return jsonify(Error="End date must be greater than start date"), 400
        # ** Checking disponibility
        daoRu = RoomUnavailable_Model_Dao()
        not_disponibility = daoRu.RoomUnavailable_Time_put(rid, ruid)
        startdate_date = datetime.strptime(startdate, '%Y-%m-%d').date()
        if not_disponibility[0] >= startdate_date:
            return jsonify(Error=f"Room is not available during the selected dates. "
                                 f"not_disponibility = {not_disponibility[0]} vs "
                                 f"startdate = {startdate}"), 400

        clid = reserve_data['clid']
        daoC = Client_Model_Dao()
        client_info = daoC.Get_Client(clid)
        if not client_info:
            return jsonify(Error="Client not found."), 404

        daoRE = Reserve_Model_Dao()
        total_cost_auto = daoRE.Get_Total_Cost(rid, clid, startdate, enddate)

        payment = reserve_data['payment']
        if payment:
            daoRu1 = RoomUnavailable_Model_Dao()
            roomunavailable = daoRu1.Put_RoomUnavailable(ruid, rid, startdate, enddate)
            controller_handler_ruid = RoomUnavailable_Controller_Handler()
            roomunavailable_result = controller_handler_ruid.RoomUnavailable_Build(ruid, rid, startdate, enddate)

            daoRe1 = Reserve_Model_Dao()
            reserve = daoRe1.Put_Reserve(ruid, clid, total_cost_auto, payment, guests, reid)
            reserve_result = self.Reserve_Build(reid, ruid, clid, total_cost_auto, payment, guests)

            return jsonify(Reserve=reserve_result, RoomUnavailable=reserve_result), 200
        else:
            return jsonify("Unexpected attribute values."), 400

    def Delete_Reserve(self, reserve_id):
        daoRe = Reserve_Model_Dao()
        reserve_info = daoRe.Get_Reserve(reserve_id)
        if not reserve_info:
            return jsonify(Error="Reserve not found."), 404

        daoRe1 = Reserve_Model_Dao()
        result = daoRe1.Delete_Reserve(reserve_id)
        if result == 'Error deleting':
            return jsonify(Error="Reserve is referenced"), 400
        elif result:
            ruid = reserve_info[1]
            daoRU1 = RoomUnavailable_Model_Dao()
            delete_ruid = daoRU1.Delete_RoomUnavailable(ruid)
            if not delete_ruid:
                return jsonify(Error="Room Unavailable not deleted"), 500
            return jsonify(OK=f"Reserve {reserve_id} and Room Unavailable {ruid} deleted"), 200
        else:
            return jsonify(Error="Delete Failed"), 500
