# ** Importing necessary modules
from model_dao.employee import Employee_Model_Dao
from model_dao.login import Login_Model_Dao
from flask import jsonify


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

    # ** Method to build a Login data holder

    def Login_Build(self, login_id, eid, username, password):
        login_build = {
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
        return jsonify(logins=result)

    # ** Method to retrieve a specific login by its ID
    def Get_Login(self, login_id):
        dao = Login_Model_Dao()
        login = dao.Get_Login(login_id)
        if login:
            result = self.Login_Dict(login)
            return jsonify(login=result)
        return jsonify("Not Found"), 404

    def Post_Login(self, login_data):
        if len(login_data) != 3:
            return jsonify(Error="Invalid Data"), 400
        # ** Models/Daos to use
        daoe = Employee_Model_Dao()
        daol = Login_Model_Dao()
        # ** Data received
        eid = login_data['eid']
        username = login_data['username']
        password = login_data['password']
        # ** Search chid if exists
        if not daoe.Get_Employee(eid):
            return jsonify(Error="Employee doesn't work with us."), 404
        if username and password:
            login_id = daol.Post_Login(eid, username, password)
            result = self.Login_Build(login_id, eid, username, password)
            return jsonify(hotel=result), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def Put_Login(self, lid, login_data):
        if len(login_data) != 3:
            return jsonify(Error="Invalid Data"), 400
            # ** Models/Daos to use
        daoe = Employee_Model_Dao()
        daol = Login_Model_Dao()
        # ** Data received
        eid = login_data['eid']
        username = login_data['username']
        password = login_data['password']
        # ** Search chid if exists
        if not daoe.Get_Employee(eid):
            return jsonify(Error="Employee doesn't work with us."), 404
        if (lid or eid == 0) and username and password:
            count = daol.Put_Login(lid, eid, username, password)
            if count > 0:
                return jsonify(Message="Your login info has been successfully changed!"), 200
            else:
                return jsonify(Error="Username or Password are incorrect. Try again."), 404
        else:
            return jsonify(Error="Incorrect field. Try again."), 400

    def Delete_Login(self, lid):
        if lid or lid == 0:
             dao = Login_Model_Dao()
             result = dao.Delete_Login(lid)
             if result == "We couldn't delete your information, sorry!":
                 return jsonify("Something went wrong, please try again."), 400
             elif result:
                 return jsonify("Deleted!"), 200
             else:
                 return jsonify("This account doesn't exist."), 404
        else:
             return jsonify("Oops, something went wrong! Try again."), 400
