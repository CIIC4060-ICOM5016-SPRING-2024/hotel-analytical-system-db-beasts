from model_dao.LocalStatistics import LocalStatistics_Model_Dao
from model_dao.employee import Employee_Model_Dao
from model_dao.hotel import Hotel_Model_Dao

from flask import jsonify


class LocalStatistics_Controller_Handler:

    # * ROOMTYPE
    def RoomType_Dict(self, r):
        roomtype_dict = {
            'hid': r[0],
            'room type': r[1],
            'total reserves': r[2]
        }
        return roomtype_dict

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

    # * MOSTCREDITCARD
    def MostCreditCard_Dict(self, r):
        mostcreditcard_dict = {
            'clid': r[0],
            'age': r[1],
            'hid': r[2],
            'chid': r[3],
            'payment': r[4],
            'total reserves': r[5]
        }
        return mostcreditcard_dict

    # * MOSTCREDITCARD
    def Get_post_MostCreditCard(self, hid, employee_id):
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
            mostcreditcards = daoLS.Get_post_MostCreditCard(hid)
            result = []
            for mostcreditcard in mostcreditcards:
                result.append(self.MostCreditCard_Dict(mostcreditcard))
            return jsonify(Most_Credit_Cards=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            mostcreditcards = daoLS.Get_post_MostCreditCard(hid)
            result = []
            for mostcreditcard in mostcreditcards:
                result.append(self.MostCreditCard_Dict(mostcreditcard))
            return jsonify(Most_Credit_Cards=result), 200
        # ** If the employee is an administrator
        mostcreditcards = daoLS.Get_post_MostCreditCard(hid)
        result = []
        for mostcreditcard in mostcreditcards:
            result.append(self.MostCreditCard_Dict(mostcreditcard))
        return jsonify(Most_Credit_Cards=result), 200

    # * HANDICAPROOM
    def HandicapRoom_Dict(self, r):
        handicaproom_dict = {
            'hid': r[0],
            'rid': r[1],
            'rname': r[2],
            'rtype': r[3],
            'ishandicap': r[4],
            'total reserves': r[5]
        }
        return handicaproom_dict

    # * HANDICAPROOM
    def Get_post_HandicapRoom(self, hid, employee_id):
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
            handicaprooms = daoLS.Get_post_HandicapRoom(hid)
            result = []
            for handicaproom in handicaprooms:
                result.append(self.HandicapRoom_Dict(handicaproom))
            return jsonify(Total_HandicapRooms=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            handicaprooms = daoLS.Get_post_HandicapRoom(hid)
            result = []
            for handicaproom in handicaprooms:
                result.append(self.HandicapRoom_Dict(handicaproom))
            return jsonify(Total_HandicapRooms=result), 200
        # ** If the employee is an administrator
        handicaprooms = daoLS.Get_post_HandicapRoom(hid)
        result = []
        for handicaproom in handicaprooms:
            result.append(self.HandicapRoom_Dict(handicaproom))
        return jsonify(Total_HandicapRooms=result), 200

    # * LEASTRESERVE
    def LeastReserve_Dict(self, r):
        leastreserve_dict = {
            'hid': r[0],
            'rid': r[1],
            'rname': r[2],
            'rtype': r[3],
            'unavailable': r[4],
        }
        return leastreserve_dict

    # * LEASTRESERVE
    def Get_post_LeastReserve(self, hid, employee_id):
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
            leastreserves = daoLS.Get_post_LeastReserve(hid)
            result = []
            for leastreserve in leastreserves:
                result.append(self.LeastReserve_Dict(leastreserve))
            return jsonify(Least_Reserves=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            leastreserves = daoLS.Get_post_LeastReserve(hid)
            result = []
            for leastreserve in leastreserves:
                result.append(self.LeastReserve_Dict(leastreserve))
            return jsonify(Least_Reserves=result), 200
        # ** If the employee is an administrator
        leastreserves = daoLS.Get_post_LeastReserve(hid)
        result = []
        for leastreserve in leastreserves:
            result.append(self.LeastReserve_Dict(leastreserve))
        return jsonify(Least_Reserves=result), 200

    # * LEASTGUESTS
    def LeastGuests_Dict(self, r):
        leastguests_dict = {
            'hid': r[0],
            'rid': r[1],
            'rname': r[2],
            'rtype': r[3],
            'guests:capacity': r[4],
            'space': r[5]
        }
        return leastguests_dict

    # * LEASTGUESTS
    def Get_post_LeastGuests(self, hid, employee_id):
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
            leastguests = daoLS.Get_post_LeastGuests(hid)
            result = []
            for leastguest in leastguests:
                result.append(self.LeastGuests_Dict(leastguest))
            return jsonify(Least_Guests=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            leastguests = daoLS.Get_post_LeastGuests(hid)
            result = []
            for leastguest in leastguests:
                result.append(self.LeastGuests_Dict(leastguest))
            return jsonify(Least_Guests=result), 200
        # ** If the employee is an administrator
        leastguests = daoLS.Get_post_LeastGuests(hid)
        result = []
        for leastguest in leastguests:
            result.append(self.LeastGuests_Dict(leastguest))
        return jsonify(Least_Guests=result), 200

    # * HIGHESTPAID
    def HighestPaid_Dict(self, r):
        highestpaid_dict = {
            'hid': r[0],
            'eid': r[1],
            'full name': r[2],
            'position': r[3],
            'salary': r[4]
        }
        return highestpaid_dict

    # * HIGHESTPAID
    def Get_post_HighestPaid(self, hid, employee_id):
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
            highestpaids = daoLS.Get_post_HighestPaid(hid)
            result = []
            for highestpaid in highestpaids:
                result.append(self.HighestPaid_Dict(highestpaid))
            return jsonify(Highest_Paids=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            highestpaids = daoLS.Get_post_HighestPaid(hid)
            result = []
            for highestpaid in highestpaids:
                result.append(self.HighestPaid_Dict(highestpaid))
            return jsonify(Highest_Paids=result), 200
        # ** If the employee is an administrator
        highestpaids = daoLS.Get_post_HighestPaid(hid)
        result = []
        for highestpaid in highestpaids:
            result.append(self.HighestPaid_Dict(highestpaid))
        return jsonify(Highest_Paids=result), 200

    # * MOSTDISCOUNT
    def MostDiscount_Dict(self, r):
        mostdiscount_dict = {
            'hid': r[0],
            'clid': r[1],
            'fname': r[2],
            'lname': r[3],
            'memberyear': r[4],
            'discount percentage': r[5],
            'all payments': r[6],
            'not discount': r[7],
            'discount': r[8]
        }
        return mostdiscount_dict

    # * MOSTDISCOUNT
    def Get_post_MostDiscount(self, hid, employee_id):
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
            mostdiscounts = daoLS.Get_post_MostDiscount(hid)
            result = []
            for mostdiscount in mostdiscounts:
                result.append(self.MostDiscount_Dict(mostdiscount))
            return jsonify(Most_Discounts=result), 200
        elif employee[5] == "Supervisor":
            # ** Check the hotel information where the employee works
            daoH1 = Hotel_Model_Dao()
            hotel1 = daoH1.Get_Hotel(employee[1])
            # ** Check if the employee works for the same chain as the searched hotel.
            if hotel1[1] != hotel[1]:
                return jsonify(Error=f"Hotel not part of a chain. {hotel1[1]} != {hotel[1]}"), 404
            mostdiscounts = daoLS.Get_post_MostDiscount(hid)
            result = []
            for mostdiscount in mostdiscounts:
                result.append(self.MostDiscount_Dict(mostdiscount))
            return jsonify(Most_Discounts=result), 200
        # ** If the employee is an administrator
        mostdiscounts = daoLS.Get_post_MostDiscount(hid)
        result = []
        for mostdiscount in mostdiscounts:
            result.append(self.MostDiscount_Dict(mostdiscount))
        return jsonify(Most_Discounts=result), 200
