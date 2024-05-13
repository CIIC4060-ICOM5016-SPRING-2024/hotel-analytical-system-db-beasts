# ** Importing necessary modules
from model_dao.employee import Employee_Model_Dao
from flask import jsonify

from model_dao.hotel import Hotel_Model_Dao
from model_dao.login import Login_Model_Dao


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
            'eid': employee_id,
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
        if len(employee_data) != 8:
            return jsonify(Error="Invalid Data"), 400

        # ** Models/Daos to use
        daoh = Hotel_Model_Dao()
        daoe = Employee_Model_Dao()
        daol = Login_Model_Dao()

        # ** Data received
        hid = employee_data['hid']
        fname = employee_data['fname']
        lname = employee_data['lname']
        age = employee_data['age']
        position = employee_data['position']
        salary = employee_data['salary']
        username = employee_data['username']
        password = employee_data['password']

        # if hid == -1:
        #     position = "Administrator"

        # if position == "Administrator":
        #    hid = -1

        error_messages = []

        # Check if hid is valid for the position
        if hid == -1 and position != "Administrator":
            error_messages.append("Incorrect position for the hotel id.")
        elif hid != -1 and position == "Administrator":
            error_messages.append("Incorrect position for the hotel id.")

            # ** Search hid if it's a valid hotel
        if not daoh.Get_Hotel(hid):
            error_messages.append("Hotel not found")

        # Validate salary based on position
        if position == "Regular" and not (18000 <= salary <= 49999):
            error_messages.append("Invalid salary range for Regular position")
        elif position == "Supervisor" and not (50000 <= salary <= 79999):
            error_messages.append("Invalid salary range for Supervisor position")
        elif position == "Administrator" and not (80000 <= salary <= 120000):
            error_messages.append("Invalid salary range for Administrator position")

        # Check if any errors occurred
        if error_messages:
            return jsonify(Error=error_messages), 400

        # Create the employee entry
        employee_id = daoe.Post_Employee(hid, fname, lname, age, position, salary)

        # Create the account for the employee
        account_id = daol.Post_Login(employee_id, username,
                                     password)  # Call the Post_Login method to create the account
        if account_id == "Error":
            daoE1 = Employee_Model_Dao()
            employee_deleted = daoE1.Delete_Employee(employee_id)
            return jsonify(Error="The employee was not created because the "
                                 "Login username exist."), 404

        result = self.Employee_Build(employee_id, hid, fname, lname, age, position, salary)
        result['username'] = username
        result['password'] = password

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

        daoe = Employee_Model_Dao()
        if daoe.Get_Employee(eid):
            daol = Login_Model_Dao()
            daolid = Login_Model_Dao()
            daoed = Employee_Model_Dao()

            # Search for the account linked to the employee ID (eid)
            login_id = daolid.Get_ID_Login(eid)

            if login_id is not None:
                # Delete the account
                daol.Delete_Login(login_id)

            # Delete the employee entry
            result = daoed.Delete_Employee(eid)

            if result:
                return jsonify("This employee has been removed with it's account from the database"), 200
            else:
                return jsonify("Not an employee"), 404
        else:
            return jsonify("Unable to find and delete this employee."), 400

    def Check_Employee(self, data):
        eid = data['eid']
        fname = data['fname']
        lname = data['lname']
        dao = Employee_Model_Dao()
        employee = dao.Get_Employee(eid)
        if not employee:
            return jsonify(Error="Not Found"), 404
        dao1 = Employee_Model_Dao()
        employee_in = dao1.Check_Employee(eid, fname, lname)
        if employee_in:
            result = self.Employee_Dict(employee_in)
            return jsonify(Employee=result), 200
        return jsonify(Error="First name or last name not valid"), 404