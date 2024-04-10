from model_dao.GlobalStatistics import GlobalStatistics_Model_Dao
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