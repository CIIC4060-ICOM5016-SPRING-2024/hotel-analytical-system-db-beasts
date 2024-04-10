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
    
    
    #HotelMethod
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

    def Get_top_10_hotelreservation(self, employee_id):
        
        if employee_id == None:
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
        
        #hid, rid,ruid,reid 
        roommap = {}
        
        for elm in result:
            hotelid = elm[0]
            if hotelid in roommap:
                roommap[hotelid] +=1
            else:
                roommap[hotelid] = 1
                
        #Get top 10 percent of hotels with most reservations
        num_of_hotels = len(roommap)
        top_10_count = int(num_of_hotels*0.1)
        
        sorted_hotels = sorted(roommap.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_hotels[:top_10_count]        
        
        
        result_dict = self.HotelMethod_Dict(top10)
        return jsonify(result=result_dict), 200
        
        
         