# ** Importing necessary modules
from flask import jsonify

from model_dao.employee import Employee_Model_Dao
from model_dao.hotel import Hotel_Model_Dao
from model_dao.login import Login_Model_Dao
from controller_handler.login import Login_Controller_Handler


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
        if len(employee_data) != 8:
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
            if fname and lname and age:

                username = employee_data['username']
                password = employee_data['password']
                if username and password:

                    daoE = Employee_Model_Dao()
                    employee_id = daoE.Post_Employee(hid, fname, lname, age, position, salary)
                    employee_result = self.Employee_Build(employee_id, hid, fname, lname, age, position, salary)

                    daoL = Login_Model_Dao()
                    login_id = daoL.Post_Login(employee_id, username, password)
                    controller_handler_login = Login_Controller_Handler()
                    login_result = controller_handler_login.Login_Build(login_id, employee_id, username, password)

                    return jsonify(OK="Employee Posted", Employee=employee_result, Login=login_result), 201

                else:
                    return jsonify(Error="Unexpected attribute values."), 400
            else:
                return jsonify(Error="Unexpected attribute values."), 400

        elif position in self.SALARY_CONSTRAINTS:
            return jsonify(Error="Invalid Salary Range"), 400
        else:
            return jsonify(Error="Invalid Position"), 400

    def Put_Employee(self, eid, employee_data):
        if len(employee_data) != 6:
            return jsonify(Error="Invalid Data"), 400

        daoE = Employee_Model_Dao()
        if not daoE.Get_Employee(eid):
            return jsonify(Error="Employee Not Found"), 404

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

            daoE1 = Employee_Model_Dao()
            employee = daoE1.Put_Employee(eid, hid, fname, lname, age, position, salary)
            result = self.Employee_Build(eid, hid, fname, lname, age, position, salary)
            return jsonify(OK="Employee Updated", Employee=result), 201

        elif position in self.SALARY_CONSTRAINTS:
            return jsonify(Error="Invalid Salary Range"), 400
        else:
            return jsonify(Error="Invalid Position"), 400

    def Delete_employee(self, employee_id):
        daoE = Employee_Model_Dao()
        if not daoE.Get_Employee(employee_id):
            return jsonify(Error="Employee Not Found"), 404

        daoL = Login_Model_Dao()
        login_id = daoL.Get_Login_ByEmployee(employee_id)
        if not login_id:
            login_id = "None"
        else:
            login_id = login_id[0]
        daoL1 = Login_Model_Dao()
        login_result = daoL1.Delete_Login(login_id)

        daoE1 = Employee_Model_Dao()
        employee_result = daoE1.Delete_Employee(employee_id)
        # if employee_result == "Error":
        #     return jsonify(Error="Employee is referenced"), 400
        if employee_result:
            return jsonify(OK=f"Employee {employee_id} and Login {login_id} Deleted"), 200
        else:
            return jsonify(Error="Delete Failed"), 500

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
