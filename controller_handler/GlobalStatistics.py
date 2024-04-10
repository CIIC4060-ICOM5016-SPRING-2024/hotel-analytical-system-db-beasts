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


    #** TOP 3 CHAINS WIth LESS ROOMS
    def Chains_Dict(self, chain):
        chains_dict = {
            'chid': chain[0],
            'cname': chain[1],
            'springmkup': chain[2],
            'summermkup': chain[3],
            'fallmkup': chain[4],
            'wintermkup': chain[5],
            'room_count': chain[6]
        }
        return chains_dict

    # ** TOP 5 CLIENTS WITH DISCOUNTS
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
            result.append(self.Hotels_Dict(hotels,))

        return jsonify(Top_Three_Chains=result), 200

