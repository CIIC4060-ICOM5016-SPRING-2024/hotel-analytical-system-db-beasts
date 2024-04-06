# ** Importing necessary modules
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
