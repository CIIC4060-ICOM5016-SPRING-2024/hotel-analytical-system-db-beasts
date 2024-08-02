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

    # * TOP5_HANDICAPROOM
    def Top5_HandicapRoom_Dict(self, r):
        top5_handicaproom_dict = {
            'rooms': []  # Placeholder for top 5 room information
        }

        # Add room information to the 'rooms' list
        for room in r:
            top5_handicaproom_dict['rooms'].append({
                'room_id': room[0],
                'chid': room[1],
                'total_reserves': room[2],

            })

        return top5_handicaproom_dict

    def least_reserved_room_Dict(self, r):
        least_reserved_room_dict = {
            'rooms': []  # Placeholder for top 5 room information
        }

        # Add room information to the 'rooms' list
        for room in r:
            least_reserved_room_dict['rooms'].append({
                'rid': room[0],
                'chid': room[1],
                'days_reserved': room[2],
            })

        return least_reserved_room_dict

    # * LEASTRESERVE
    def Highest_Paid_Dict(self, emp):
        highestregpaid_dict = {
            
            'eid': emp[0],
            'hid': emp[1],
            'fname': emp[2],
            'lname': emp[3],
            'age': emp[4],
            'position': emp[5],
            'salary': emp[6]
        }
        return highestregpaid_dict

    # Hotel
    # Top 5 handicap rooms that were reserve the most.
    def Get_post_top5_HandicapRoom(self, hid, employee_id):

        if not isinstance(employee_id, dict) or 'eid' not in employee_id:
            return jsonify(Error="Invalid employee data"), 400

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

        employee_role = employee[5]
        employee_works_at = employee[1]
        daoH = Hotel_Model_Dao()
        hotel_chid = daoH.Get_Hotels_Chain(hid)
        if employee_role != "Administrator":
            daoH = Hotel_Model_Dao()
            employee_chid = daoH.Get_Hotels_Chain(employee_works_at)
            if employee_role == "Regular" and employee_works_at != hid:
                return jsonify(Error="Employee is not part of the hotel."), 404

            if employee_role == "Supervisor" and employee_chid != hotel_chid:
                return jsonify(Error="Employee cannot view statistics from different chains."), 404

        localdao = LocalStatistics_Model_Dao()
        rooms = localdao.Get_handicap_rooms(hid)

        if rooms is None:
            return jsonify(Error="No rooms found"), 404

        # Data order hid,chid,rid,reid as total_reserve,ishandicap as handicap_room
        roommap = {}
        for room in rooms:
            rid = room[2]
            chid = room[1]
            if rid not in roommap:
                roommap[rid] = [chid, 1]
            else:
                roommap[rid][1] += 1

        rooms = []
        for key, value in roommap.items():
            room = [key, value[0], value[1]]
            rooms.append(room)

        rooms = sorted(rooms, key=lambda x: x[2], reverse=True)[:5]
        rooms_dict = self.Top5_HandicapRoom_Dict(rooms)
        return jsonify(Top5_HandicapRoom=rooms_dict), 200

    def Get_leastreserve_Room(self, hid, employee_id):

        # ** Check if there is a credential
        if not isinstance(employee_id, dict) or 'eid' not in employee_id:
            return jsonify(Error="Invalid employee data"), 400

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

        employee_role = employee[5]
        employee_works_at = employee[1]
        daoH = Hotel_Model_Dao()
        hotel_chid = daoH.Get_Hotels_Chain(hid)
        if employee_role != "Administrator":
            daoH = Hotel_Model_Dao()
            employee_chid = daoH.Get_Hotels_Chain(employee_works_at)

            # ** Check employee can view data
            if employee_role == "Regular" and employee_works_at != hid:
                return jsonify(Error="Employee does not work at the hotel."), 404

            if employee_role == "Supervisor" and employee_chid != hotel_chid:
                return jsonify(Error="Employee cannot view statistics from different chains."), 404

        localdao = LocalStatistics_Model_Dao()
        rooms_availability = localdao.Get_room_availability_by_hotel(hid)
        # Check if there is any data
        if type(rooms_availability) == type(None):
            return jsonify(Error="No room reservation data found"), 404

        roommap = {}

        # Order of elements
        # hid,chid,rid,startdate, enddate
        for room in rooms_availability:
            rid = room[2]
            chid = room[1]
            if rid in roommap:
                roommap[rid][1] += (room[4] - room[3]).days
            else:
                internal_dat = [chid, (room[4] - room[3]).days]
                roommap[rid] = internal_dat

        rooms = []
        for key, value in roommap.items():
            room = [key, value[0], value[1]]
            rooms.append(room)

        # Sort by least reserved and limit to 3
        sortedrooms = sorted(rooms, key=lambda x: x[2])[:3]
        # Create dictionary model
        sortedrooms_dict = self.least_reserved_room_Dict(sortedrooms)
        return jsonify(sortedrooms=sortedrooms_dict), 200

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
        # return jsonify(Total_Hotel_Reserves=result), 200

    # * HIGHESTPAID REGULAR EMPLOYEE
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

    # * LEASTGUESTS
    def LeastGuests_Dict(self, r):
        leastguests_dict = {
            'hid': r[0],
            'rid': r[1],
            'room': r[2],
            'ratio': r[3]
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
