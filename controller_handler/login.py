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
            'lid': login_id,
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
        eid = login_data['eid']
        daoe = Employee_Model_Dao()
        if not daoe.Get_Employee(eid):
            return jsonify(Error="Employee doesn't work with us."), 404
        daol = Login_Model_Dao()
        login_id_employee = daol.Get_Login_ByEmployee(eid)
        if not login_id_employee:
            username = login_data['username']
            password = login_data['password']
            if username and password:
                daol1 = Login_Model_Dao()
                login_id = daol1.Post_Login(eid, username, password)
                if login_id == "Error":
                    return jsonify(Error="Login could not be post because the username exist."), 404
                result = self.Login_Build(login_id, eid, username, password)
                return jsonify(Login=result, OK="Loin Posted Successfully"), 201
            else:
                return jsonify("Unexpected attribute values."), 400
        else:
            return jsonify(Error="Employee have login account"), 400

    def Put_Login(self, lid, login_data):
        if len(login_data) != 2:
            return jsonify(Error="Invalid Data entered."), 400

        daol = Login_Model_Dao()
        username = login_data.get('username')
        password = login_data.get('password')

        if username and password:
            count = daol.Put_Login(lid, username, password)  # Pass lid, username, and password as parameters
            if count == "Error":
                return jsonify(Error="Login could not be put because the username exist."), 404
            elif count > 0:
                return jsonify("Your login info has been successfully changed!"), 200
            else:
                return jsonify(Error="This account doesn't exist. Please create it first!"), 404
        else:
            return jsonify(Error="Username or Password is incorrect. Try again."), 400

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

    '''
    ------------------
    * THIRD PHASE
    ------------------
    '''

    # ** Method to verify if the user input for the
    # ** password and username are correct compared to
    # ** the ones in the database
    def LogIn_Verification(self, authentication):
        username, password = authentication['username'], authentication['password']
        dao = Login_Model_Dao()
        login = dao.LogIn_Check(username, password)
        if login is not None:
            result = self.Login_Dict(login)
            return jsonify(login=result), 200
        else:
            return jsonify(error="Invalid username or password"), 400
