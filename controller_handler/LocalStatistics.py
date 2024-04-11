from model_dao.LocalStatistics import LocalStatistics_Model_Dao
from model_dao.employee import Employee_Model_Dao
from model_dao.hotel import Hotel_Model_Dao

from flask import jsonify


class LocalStatistics_Controller_Handler:

    # * ROOMTYPE
    def RoomType_Dict(self, r):
        roomtype_dict = {
            'hotel': r[0],
            'room type': r[1],
            'total reserves': r[2]
        }
        return roomtype_dict


    # * LEASTRESERVE
    def Highest_Paid_Dict(self, emp):
        highestregpaid_dict = {
            'hid': emp[0],
            'eid': emp[1],
            'fname': emp[2],
            'lname': emp[3],
            'position': emp[4],
            'salary': emp[5]
        }
        return highestregpaid_dict

    # * ROOMTYPE
    def Get_post_RoomType(self, hid, employee_id):
        # ** Check if there is a credential
        if len(employee_id) != 1:
            return jsonify(Error="Invalid Data"), 400
        # ** Check if the searched hotel exists
        daoH = Hotel_Model_Dao()
        hotel = daoH.Get_Hotel(hid)
        if not hotel:
            return jsonify(Error="Hotel not found"), 404
        # ** Check if the employee exists and their information
        eid = employee_id['eid']
        daoE = Employee_Model_Dao()
        employee = daoE.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found"), 404
        daoLS = LocalStatistics_Model_Dao()
        # ** Check employee position
        if employee[5] == "Regular":
            # ** Check if the employee works at the hotel that are looking for
            if employee[1] != hid:
                return jsonify(Error="Employee is not part of the hotel."), 404
            roomtypes = daoLS.Get_post_RoomType(hid)
            result = []
            for roomtype in roomtypes:
                result.append(self.RoomType_Dict(roomtype))
            return jsonify(Total_Hotel_Reserves=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            roomtypes = daoLS.Get_post_RoomType(hid)
            result = []
            for roomtype in roomtypes:
                result.append(self.RoomType_Dict(roomtype))
            return jsonify(Total_Hotel_Reserves=result), 200
        # ** If the employee is an administrator
        roomtypes = daoLS.Get_post_RoomType(hid)
        result = []
        for roomtype in roomtypes:
            result.append(self.RoomType_Dict(roomtype))
        return jsonify(Total_Hotel_Reserves=result), 200

  # * LEASTRESERVE
    def Get_post_Highest_Paid_Regular_Employees(self, hid, employee_id):
        # ** Check if there is a credential
        if len(employee_id) != 1:
            return jsonify(Error="Invalid Data"), 400
        # ** Check if the searched hotel exists
        daoH = Hotel_Model_Dao()
        hotel = daoH.Get_Hotel(hid)
        if not hotel:
            return jsonify(Error="Hotel not found"), 404
        # ** Check if the employee exists and their information
        eid = employee_id['eid']
        daoE = Employee_Model_Dao()
        employee = daoE.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found"), 404
        daoLS = LocalStatistics_Model_Dao()
        # ** Check employee position
        if employee[5] == "Regular":
            # ** Check if the employee works at the hotel that are looking for
            if employee[1] != hid:
                return jsonify(Error="Employee is not part of the hotel."), 404
            highestpaids = daoLS.Get_post_Highest_Paid_Regular_Employees(hid)
            result = []
            for highestpaid in highestpaids:
                result.append(self.Highest_Paid_Dict(highestpaid))
            return jsonify(Highest_Paid_Regular_Employees=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            highestpaids = daoLS.Get_post_Highest_Paid_Regular_Employees(hid)
            result = []
            for highestpaid in highestpaids:
                result.append(self.Highest_Paid_Dict(highestpaid))
            return jsonify(Highest_Paid_Regular_Employees=result), 200
        # ** If the employee is an administrator
        highestpaids = daoLS.Get_post_Highest_Paid_Regular_Employees(hid)
        result = []
        for highestpaid in highestpaids:
            result.append(self.Highest_Paid_Dict(highestpaid))
        return jsonify(Highest_Paid_Regular_Employees=result), 200