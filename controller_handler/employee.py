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

    def Employee_Build(self, eid, hid, fname, lname, age, position, salary):
        employee_build = {
            'eid': eid,
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
        return jsonify(Employees=result)

    # ** Method to retrieve a specific employee by its ID
    def Get_Employee(self, employee_id):
        dao = Employee_Model_Dao()
        employee = dao.Get_Employee(employee_id)
        if employee:
            result = self.Employee_Dict(employee)
            return jsonify(Employee=result)
        return jsonify(Error="Not Found"), 404

    def Post_Employee(self, employee_data):
        if len(employee_data) != 6:
            return jsonify(Error="Invalid Data"), 400

        hid = employee_data['hid']
        daoH = Hotel_Model_Dao()
        hotel_info = daoH.Get_Hotel(hid)
        if not hotel_info:
            return jsonify(Error="Hotel Not Found"), 404

        position = employee_data['position']
        salary = employee_data['salary']
        if self.is_valid_salary(position, salary):

            fname = employee_data['fname']
            lname = employee_data['lname']
            age = employee_data['age']

            daoE = Employee_Model_Dao()
            employee_id = daoE.Post_Employee(hid, fname, lname, age, position, salary)
            result = self.Employee_Build(employee_id, hid, fname, lname, age, position, salary)
            return jsonify(Employee=result), 201

        elif position in self.SALARY_CONSTRAINTS:
            return jsonify(Error="Invalid Salary Range"), 400
        else:
            return jsonify(Error="Invalid Position"), 400

    """
    ------------------
    * TOOL OPERATIONS
    ------------------
    """

    SALARY_CONSTRAINTS = {
        "Regular": (18000, 49999),
        "Supervisor": (50000, 79999),
        "Administrator": (80000, 120000),
    }

    def is_valid_salary(self, position, salary):
        min_salary, max_salary = self.SALARY_CONSTRAINTS.get(position, (None, None))
        return min_salary <= salary <= max_salary if min_salary is not None else False
