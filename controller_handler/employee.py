# Importing necessary modules
from model_dao.employee import Employee_Model_Dao
from flask import jsonify


# Class for handling HTTP requests related to employee
class Employee_Controller_Handler:
    # Method to create a dictionary representation of chain data
    def Employee_Dict(self, r):
        employee_dict = {
            'eid': r[0],
            'hid': r[1],
            'fname': r[2],
            'lname': r[3],
            'age': r[4],
            'position': r[5],
            'salary': r[6]
        }
        return employee_dict

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    def Get_All_Employees(self):
        dao = Employee_Model_Dao()
        employees = dao.Get_All_Employees()
        result = []
        for employee in employees:
            result.append(self.Employee_Dict(employee))
        return jsonify(employees=result)
