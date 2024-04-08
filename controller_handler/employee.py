# ** Importing necessary modules
from model_dao.employee import Employee_Model_Dao
from flask import jsonify

from model_dao.hotel import Hotel_Model_Dao


# ** Class for handling HTTP requests related to employee
class Employee_Controller_Handler:
    # ** Method to create a dictionary representation of employee data
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

    # ** Method to build an Employee data holder

    def Employee_Build(self, employee_id, hid, fname, lname, age, position, salary):
        employee_build = {
            'hid': hid,
            'fname': fname,
            'lname': lname,
            'age': age,
            'position': position,
            'salary': salary
        }
        return employee_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all employees
    def Get_All_Employees(self):
        dao = Employee_Model_Dao()
        employees = dao.Get_All_Employees()
        result = []
        for employee in employees:
            result.append(self.Employee_Dict(employee))
        return jsonify(employees=result)

    # ** Method to retrieve a specific employee by its ID
    def Get_Employee(self, employee_id):
        dao = Employee_Model_Dao()
        employee = dao.Get_Employee(employee_id)
        if employee:
            result = self.Employee_Dict(employee)
            return jsonify(employee=result)
        return jsonify("Not Found"), 404

    # ** Method to add a new employee
    def Post_Employee(self, employee_data):
        if len(employee_data) != 6:
            return jsonify(Error="Invalid Data"), 400

        # ** Models/Daos to use
        daoh = Hotel_Model_Dao()
        daoe = Employee_Model_Dao()

        # ** Data received
        hid = employee_data['hid']
        fname = employee_data['fname']
        lname = employee_data['lname']
        age = employee_data['age']
        position = employee_data['position']
        salary = employee_data['salary']

        # ** Search hid if it's a valid hotel
        if not daoh.Get_Hotel(hid):
            return jsonify(Error="Hotel not found"), 404
        employee_id = daoe.Post_Employee(hid, fname, lname, age, position, salary)
        result = self.Employee_Build(employee_id, hid, fname, lname, age, position, salary)
        return jsonify(employee=result), 201

    # ** Method to update an existing employee

    def Put_Employee(self, eid, employee_data):
        if len(employee_data) != 6:
            return jsonify(Error="Invalid Data"), 400

        # ** Models/Daos to use
        daoh = Hotel_Model_Dao()
        daoe = Employee_Model_Dao()

        # ** Data received
        hid = employee_data['hid']
        fname = employee_data['fname']
        lname = employee_data['lname']
        age = employee_data['age']
        position = employee_data['position']
        salary = employee_data['salary']

        # ** Search hid if it's a valid hotel
        if not daoh.Get_Hotel(hid):
            return jsonify(Error="Hotel not found"), 404
        if (eid or hid == 0) and fname and lname and age and position and salary:
            count = daoe.Put_Employee(eid, hid, fname, lname, age, position, salary)
            if count > 0:
                return jsonify(Message="Employee updated successfully"), 200
            else:
                return jsonify(Error="Employee not found"), 404
        else:
            return jsonify(Error="Unexpected attribute values."), 400


 # ** Method to fire an employee (Delete)
    def Delete_Employee(self, eid):
        if eid or eid == 0:
            dao = Employee_Model_Dao()
            result = dao.Delete_Employee(eid)
            if result == "Error deleting the employee":
                return jsonify("This employee has connections, it's untouchable."), 400
            elif result:
                return jsonify("Fired"), 200
            else:
                return jsonify("Not an Employee"), 404
        else:
            return jsonify("Unable to fire this employee."), 400

