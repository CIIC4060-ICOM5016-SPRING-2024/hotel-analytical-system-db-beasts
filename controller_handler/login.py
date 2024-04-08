# ** Importing necessary modules
from flask import jsonify

from model_dao.login import Login_Model_Dao
from model_dao.employee import Employee_Model_Dao
# from controller_handler.employee import Employee_Controller_Handler


# ** Class for handling HTTP requests related to login
class Login_Controller_Handler:
    # ** Method to create a dictionary representation of login data
    def Login_Dict(self, r):
        login_dict = {
            'lid': r[0],
            'eid': r[1],
            'username': r[2],
            'password': r[3]
        }
        return login_dict

    def Login_Build(self, lid, eid, username, password):
        login_build = {
            'lid': lid,
            'eid': eid,
            'username': username,
            'password': password
        }
        return login_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all logins
    def Get_All_Logins(self):
        dao = Login_Model_Dao()
        logins = dao.Get_All_Logins()
        result = []
        for login in logins:
            result.append(self.Login_Dict(login))
        return jsonify(Logins=result)

    # ** Method to retrieve a specific login by its ID
    def Get_Login(self, login_id):
        dao = Login_Model_Dao()
        login = dao.Get_Login(login_id)
        if login:
            result = self.Login_Dict(login)
            return jsonify(Login=result)
        return jsonify(Error="Not Found"), 404

    def Post_Login(self, login_data):
        if len(login_data) != 3:
            return jsonify(Error="Invalid Data"), 400

        eid = login_data['eid']
        daoE = Employee_Model_Dao()
        employee_info = daoE.Get_Employee(eid)
        if not employee_info:
            return jsonify(Error="Employee not found"), 404
        # controller_handler_employee = Employee_Controller_Handler()
        # employee_result = controller_handler_employee.Employee_Dict(employee_info)

        daoL = Login_Model_Dao()
        login_id_employee = daoL.Get_Login_ByEmployee(eid)
        if not login_id_employee:
            username = login_data['username']
            password = login_data['password']
            if username and password:
                daoL1 = Login_Model_Dao()
                login_id = daoL1.Post_Login(eid, username, password)
                login_result = self.Login_Build(login_id, eid, username, password)
                return jsonify(Login=login_result, OK="Loin Posted Successfully"), 201
            else:
                return jsonify(Error="Unexpected attribute values."), 400
        else:
            return jsonify(Error="Employee have login account"), 404
