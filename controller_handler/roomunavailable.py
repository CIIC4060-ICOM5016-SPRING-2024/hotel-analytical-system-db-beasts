# ** Importing necessary modules
from model_dao.roomunavailable import RoomUnavailable_Model_Dao
from model_dao.room import Room_Model_Dao
from model_dao.employee import Employee_Model_Dao

from flask import jsonify
from datetime import datetime

# ** Class for handling HTTP requests related to RoomUnavailable
class RoomUnavailable_Controller_Handler:
    # ** Method to create a dictionary representation of RoomUnavailable data
    def RoomUnavailable_Dict(self, r):
        roomunavailable_dict = {
            'ruid': r[0],
            'rid': r[1],
            'startdate': r[2],
            'enddate': r[3]
        }
        return roomunavailable_dict

    def RoomUnavailable_Build(self, ruid, rid, startdate, enddate):
        roomunavailable_build = {
            'ruid': ruid,
            'rid': rid,
            'startdate': startdate,
            'enddate': enddate
        }
        return roomunavailable_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all RoomsUnavailable
    def Get_All_RoomsUnavailable(self):
        dao = RoomUnavailable_Model_Dao()
        roomsunavailable = dao.Get_All_RoomsUnavailable()
        result = []
        for roomunavailable in roomsunavailable:
            result.append(self.RoomUnavailable_Dict(roomunavailable))
        return jsonify(Roomsunavailable=result)

    # ** Method to retrieve a specific RoomUnavailable by its ID
    def Get_RoomUnavailable(self, roomunavailable_id):
        dao = RoomUnavailable_Model_Dao()
        roomunavailable = dao.Get_RoomUnavailable(roomunavailable_id)
        if roomunavailable:
            result = self.RoomUnavailable_Dict(roomunavailable)
            return jsonify(Roomunavailable=result)
        return jsonify(Error="Not Found"), 404

    def Post_RoomUnavailable(self, roomunavailable_data):
        if len(roomunavailable_data) != 4:
            return jsonify(Error="Invalid Data"), 400

        # ** Checking employee information
        eid = roomunavailable_data['eid']
        daoEmployee = Employee_Model_Dao()
        employee = daoEmployee.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found."), 404
        if employee[5] != "Supervisor":
            return jsonify(Error="The employee position is not Supervisor"), 401

        # ** Checking room based on the hotel where the employee works
        rid = roomunavailable_data['rid']
        daoRoom = Room_Model_Dao()
        room = daoRoom.Get_Room_Info(rid, employee[1])
        if not room:
            return jsonify(Error=f"Room not found in the hotel = {employee[1]}."), 404

        # ** Checking length of unavailable
        startdate = roomunavailable_data['startdate']
        enddate = roomunavailable_data['enddate']
        if enddate <= startdate:
            return jsonify(Error="End date must be greater than start date"), 400

        # ** Checking unavailable
        daoRU1 = RoomUnavailable_Model_Dao()
        not_disponibility = daoRU1.RoomUnavailable_Time(rid)
        startdate_date = datetime.strptime(startdate, '%Y-%m-%d').date()
        if not_disponibility[0] >= startdate_date:
            return jsonify(Error=f"Room is not available during the selected dates. "
                                 f"not_disponibility={not_disponibility[0]} vs "
                                 f"startdate={startdate}"), 400

        # ** Creating new room unavailability for the indicated dates
        daoRU2 = RoomUnavailable_Model_Dao()
        ruid = daoRU2.Post_RoomUnavailable(rid, startdate, enddate)
        if not ruid:
            return jsonify(Error="The room could not be separated."), 404
        roomunavailable_result = self.RoomUnavailable_Build(ruid, rid, startdate, enddate)
        return jsonify(Roomunavailable=roomunavailable_result), 201
