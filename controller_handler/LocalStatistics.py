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
    
    def Top5_HandicapRoom_Dict(self, r):
        top5_handicaproom_dict = {
            'hotel_id': r[0][0],
            'rooms': []  # Placeholder for top 5 room information
        }

        # Add room information to the 'rooms' list
        for room in r:
            top5_handicaproom_dict['rooms'].append({
                'room_id': room[1],
                'room_type': room[2],
                'total_reserves': room[3],
                'is_handicap': room[4]
            })

        return top5_handicaproom_dict 

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
    
    
    
    #Hotel
    #Top 5 handicap rooms that were reserve the most.
    def Get_post_HandicapRoom(self, hid, employee_id):
        """Retrieves a list of the top 5 most reserved handicap rooms for a hotel.

        Args:
            hid: The hotel ID.
            employee_id: The employee's identification information.

        Returns:
            A JSON object containing the top 5 handicap rooms and their reservation counts, 
            or an error message if applicable.
        """

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

        # ** Check employee position
        if employee[5] == "Regular":
            # ** Check if the employee works at the hotel that are looking for
            if employee[1] != hid:
                return jsonify(Error="Employee is not part of the hotel."), 404

        # ** Get handicap room reservation data
        daoLS = LocalStatistics_Model_Dao()
        room_data = daoLS.Get_post_HandicapRoom(hid)

        # **Process and return top 5 rooms**
        if type(room_data) != type(None):
            # Sort by total reserves (descending)
            top_5 = room_data[:5]
            top_5_dict = self.Top5_HandicapRoom_Dict(top_5)
            
            return jsonify(top_rooms=top_5_dict), 200
        else:
            return jsonify(Error="No handicap room reservation data found"), 404 
  
            
