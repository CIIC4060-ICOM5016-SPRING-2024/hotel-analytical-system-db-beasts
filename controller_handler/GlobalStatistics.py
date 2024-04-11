from model_dao.GlobalStatistics import GlobalStatistics_Model_Dao
from model_dao.chains import Chains_Model_Dao
from model_dao.employee import Employee_Model_Dao

from flask import jsonify


class GlobalStatistics_Controller_Handler:

    # * PAYMENTMETHOD
    def PaymentMethod_Dict(self, r):
        paymentmethod_dict = {
            'paymentmethod': r[0],
            'total reservations': r[1],
            'reservation percentage': r[2]
        }
        return paymentmethod_dict

    # * MOST_REVENUE
    def MostRevenue_Dict(self, r):
        mostrevenue_dict = {
            'chid': r[0],
            'total revenue': r[1]
        }
        return mostrevenue_dict

    # ** HotelMethod
    def HotelMethod_Dict(self, r):
        hotelmethod_dict = {
            'hotels': []

        }

        for hotel in r:
            hotelmethod_dict['hotels'].append({
                'hotel': hotel[0],
                'total reservations': hotel[1]
            })
        return hotelmethod_dict

    def Month_Dict(self, r):
        month_dict = {
            'months': []

        }

        for month in r:
            month_dict['months'].append({
                'month': month[0],
                'total reservations': month[1]
            })
        return month_dict

    # ** TOP 3 CHAINS WITH LESS ROOMS
    def Chains_Dict(self, chain):
        chains_dict = {
            'chid': chain[0],
            'cname': chain[1],
            'room_count': chain[2]
        }
        return chains_dict

    # ** TOP 5 HOTELS
    def Hotels_Dict(self, hotel):
        hotel_dict = {
            'hotel_id': hotel[0],
            'hotel_name': hotel[1],
            'total_capacity': hotel[2]
        }
        return hotel_dict

    # * PAYMENTMETHOD

    def Get_post_PaymentMethod(self, employee_id):
        # ** Check if there is a credential
        if len(employee_id) != 1:
            return jsonify(Error="Invalid Data"), 400
        # if type(employee_id) is not int:
        #     return jsonify(Error="Invalid Data"), 400
        # ** Check if the employee exists and their information
        eid = employee_id['eid']
        daoE = Employee_Model_Dao()
        employee = daoE.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found"), 404
        # ** Check employee position
        if employee[5] != "Administrator":
            return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403
        # ** All Good
        daoGS = GlobalStatistics_Model_Dao()
        paymentmethods = daoGS.Get_post_PaymentMethod()
        result = []
        for paymentmethod in paymentmethods:
            result.append(self.PaymentMethod_Dict(paymentmethod))
        return jsonify(Payment_Method_Percentage=result), 200

    # ** GETTING THE TOP 3 CHAINS WITH LESS ROOMS

    def Get_Top_Three_Chains_With_Least_Rooms(self, employee_id):
        if len(employee_id) != 1:
            return jsonify(Error="Invalid Data"), 400
        # if type(employee_id) is not int:
        #     return jsonify(Error="Invalid Data"), 400
        # ** Check if the employee exists and their information
        eid = employee_id['eid']
        daoE = Employee_Model_Dao()
        employee = daoE.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found"), 404
        # ** Check employee position
        if employee[5] != "Administrator":
            return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403
        daoC = GlobalStatistics_Model_Dao()
        chains = daoC.Get_Top_Three_Chains_With_Least_Rooms()

        result = []
        for chain in chains:
            result.append(self.Chains_Dict(chain))

        return jsonify(Top_Three_Chains=result), 200

        # ** TOP 3 HOTELS WITH MOST CAPACITY

    def Get_Top_Five_Hotels_With_Most_Capacity(self, employee_id):
        if len(employee_id) != 1:
            return jsonify(Error="Invalid Data"), 400
        # ** Check if the employee exists and their information
        eid = employee_id['eid']
        daoE = Employee_Model_Dao()
        employee = daoE.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found"), 404
        # ** Check employee position
        if employee[5] != "Administrator":
            return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403
        daoC = GlobalStatistics_Model_Dao()
        hotel = daoC.Get_Top_Five_Hotels_With_Most_Capacity()

        result = []
        for hotels in hotel:
            result.append(self.Hotels_Dict(hotels, ))

        return jsonify(Top_Five_Hotels_With_Most_Capacity=result), 200

    # ** GETTING THE TOP 3 CHAINS WITH LESS ROOMS

    # def Get_Top_Three_Chains_With_Least_Rooms(self, employee_id):
    #     if len(employee_id) != 1:
    #         return jsonify(Error="Invalid Data"), 400
    #     # if type(employee_id) is not int:
    #     #     return jsonify(Error="Invalid Data"), 400
    #     # ** Check if the employee exists and their information
    #     eid = employee_id['eid']
    #     daoE = Employee_Model_Dao()
    #     employee = daoE.Get_Employee(eid)
    #     if not employee:
    #         return jsonify(Error="Employee not found"), 404
    #     # ** Check employee position
    #     if employee[5] != "Administrator":
    #         return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403
    #     daoC = GlobalStatistics_Model_Dao()
    #     chains = daoC.Get_Top_Three_Chains_With_Least_Rooms()
    #
    #     result = []
    #     for chain in chains:
    #         result.append(self.Chains_Dict(chain))
    #
    #     return jsonify(Top_Three_Chains=result), 200

    # ** TOP 3 HOTELS WITH MOST CAPACITY

    # def Get_Top_Five_Hotels_With_Most_Capacity(self, employee_id):
    #     if len(employee_id) != 1:
    #         return jsonify(Error="Invalid Data"), 400
    #     # ** Check if the employee exists and their information
    #     eid = employee_id['eid']
    #     daoE = Employee_Model_Dao()
    #     employee = daoE.Get_Employee(eid)
    #     if not employee:
    #         return jsonify(Error="Employee not found"), 404
    #     # ** Check employee position
    #     if employee[5] != "Administrator":
    #         return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403
    #     daoC = GlobalStatistics_Model_Dao()
    #     hotel = daoC.Get_Top_Five_Hotels_With_Most_Capacity()
    #
    #     result = []
    #     for hotels in hotel:
    #         result.append(self.Hotels_Dict(hotels, ))
    #
    #     return jsonify(Top_Five_Hotels_With_Most_Capacity=result), 200

    def Get_top_10_hotelreservation(self, employee_id):

        if employee_id is None:
            return jsonify(Error="Invalid Data"), 400
        eid = employee_id['eid']
        employeedao = Employee_Model_Dao()
        employee = employeedao.Get_Employee(eid)

        if type(employee) == type(None):
            return jsonify(Error="Employee not found"), 404

        if employee[5] != "Administrator":
            return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403

        daoGS = GlobalStatistics_Model_Dao()
        result = daoGS.Get_top_10_hotelreservation()

        # hid, rid,ruid,reid
        roommap = {}

        for elm in result:
            hotelid = elm[0]
            if hotelid in roommap:
                roommap[hotelid] += 1
            else:
                roommap[hotelid] = 1

        # ** Get top 10 percent of hotels with most reservations
        num_of_hotels = len(roommap)
        top_10_count = int(num_of_hotels * 0.1)

        sorted_hotels = sorted(roommap.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_hotels[:top_10_count]

        result_dict = self.HotelMethod_Dict(top10)
        return jsonify(result=result_dict), 200

    def Get_top_3_monthly_reservation(self, data):
        if data is None:
            return jsonify(Error="Invalid Data"), 400

        eid = data['eid']
        chid = data['chid']

        if any(x is None for x in [eid, chid]):
            return jsonify(Error="Invalid Data"), 400

        employeedao = Employee_Model_Dao()
        employee = employeedao.Get_Employee(eid)

        if employee[5] != "Administrator":
            return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403

        daoGS = GlobalStatistics_Model_Dao()
        result = daoGS.Get_top_3_monthly_reservation(chid)

        monthmap = {}

        for reserve in result:
            month = reserve[2].month

            if month in monthmap:
                monthmap[month] += 1
            else:
                monthmap[month] = 1

        sorted_months = sorted(monthmap.items(), key=lambda x: x[1], reverse=True)
        top3 = sorted_months[:3]

        result = self.Month_Dict(top3)

        return jsonify(result=result), 200

    # * MOST_REVENUE
    def Get_post_MostRevenue(self, employee_id):
        # ** Check if there is a credential
        if len(employee_id) != 1:
            return jsonify(Error="Invalid Data"), 400
        # if type(employee_id) is not int:
        #     return jsonify(Error="Invalid Data"), 400
        # ** Check if the employee exists and their information
        eid = employee_id['eid']
        daoE = Employee_Model_Dao()
        employee = daoE.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Employee not found"), 404
        # ** Check employee position
        if employee[5] != "Administrator":
            return jsonify(Error=f"You are not an Administrator. {employee[5]}"), 403
        daoGS = GlobalStatistics_Model_Dao()
        mostrevenues = daoGS.Get_post_MostRevenue()
        result = []
        for mostrevenue in mostrevenues:
            result.append(self.MostRevenue_Dict(mostrevenue))
        return jsonify(Most_Revenues=result), 200
