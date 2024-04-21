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
    def MostRevenue_Dict(self, r):
        mostrevenue_dict = {
            'chid': r[0],
            'cname': r[1],
            'total revenue': r[2]
        }
        return mostrevenue_dict

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

    # * LEAST_ROOMS
    def LeastRooms_Dict(self, r):
        leastrooms_dict = {
            'chid': r[0],
            'cname': r[1],
            'total rooms': r[2]
        }
        return leastrooms_dict

    # * LEAST_ROOMS
    def Get_post_LeastRooms(self, employee_id):
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
        leastrooms = daoGS.Get_post_LeastRooms()
        result = []
        for leastroom in leastrooms:
            result.append(self.LeastRooms_Dict(leastroom))
        return jsonify(Least_Rooms=result), 200

    # * MOST_CAPACITY
    def MostCapacity_Dict(self, r):
        mostcapacity_dict = {
            'hid': r[0],
            'hname': r[1],
            'total capacity': r[2]
        }
        return mostcapacity_dict

    # * MOST_CAPACITY
    def Get_post_MostCapacity(self, employee_id):
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
        mostcapacities = daoGS.Get_post_MostCapacity()
        result = []
        for mostcapacity in mostcapacities:
            result.append(self.MostCapacity_Dict(mostcapacity))
        return jsonify(Most_Capacities=result), 200

    # * MOST_RESERVATION
    def MostReservation_Dict(self, r):
        mostreservation_dict = {
            'hid': r[0],
            'hname': r[1],
            'total reserves': r[2]
        }
        return mostreservation_dict

    # * MOST_RESERVATION
    def Get_post_MostReservation(self, employee_id):
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
        mostreservations = daoGS.Get_post_MostReservation()
        result = []
        for mostreservation in mostreservations:
            result.append(self.MostReservation_Dict(mostreservation))
        return jsonify(Most_Reservations=result), 200

    # * MOST_PROFITMONTH
    def MostProfitMonth_Dict(self, r):
        mostprofitmonth_dict = {
            'chid': r[0],
            'cname': r[1],
            'month': r[2],
            'total reserves': r[3]
        }
        return mostprofitmonth_dict

    # * MOST_PROFITMONTH
    def Get_post_MostProfitMonth(self, employee_id):
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
        mostprofitmonths = daoGS.Get_post_MostProfitMonth()
        result = []
        for mostprofitmonth in mostprofitmonths:
            result.append(self.MostProfitMonth_Dict(mostprofitmonth))
        return jsonify(Most_Profit_Months=result), 200
