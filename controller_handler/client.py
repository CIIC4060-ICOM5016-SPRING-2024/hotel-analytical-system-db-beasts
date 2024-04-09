# ** Importing necessary modules
from model_dao.client import Client_Model_Dao
from flask import jsonify


# ** Class for handling HTTP requests related to client
class Client_Controller_Handler:
    # ** Method to create a dictionary representation of client data
    def Client_Dict(self, r):
        client_dict = {
            'clid': r[0],
            'fname': r[1],
            'lname': r[2],
            'age': r[3],
            'memberyear': r[4]
        }
        return client_dict

    def Client_Build(self, clid, fname, lname, age, memberyear):
        client_build = {
            'clid': clid,
            'fname': fname,
            'lname': lname,
            'age': age,
            'memberyear': memberyear
        }
        return client_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all clients
    def Get_All_Clients(self):
        data = Client_Model_Dao()
        clients = data.Get_All_Clients()
        result = []
        for client in clients:
            result.append(self.Client_Dict(client))
        return jsonify(Clients=result)

    # ** Method to retrieve a specific client by its ID
    def Get_Client(self, client_id):
        dao = Client_Model_Dao()
        client = dao.Get_Client(client_id)
        if client:
            result = self.Client_Dict(client)
            return jsonify(Client=result)
        return jsonify(Error="Not Found"), 404

    def Post_Client(self, client_data):
        if len(client_data) != 4:
            return jsonify(Error="Invalid Data"), 400

        fname = client_data['fname']
        lname = client_data['lname']
        age = client_data['age']
        memberyear = client_data['memberyear']
        if fname and lname and age and memberyear:
            dao = Client_Model_Dao()
            client_id = dao.Post_Client(fname, lname, age, memberyear)
            result = self.Client_Build(client_id, fname, lname, age, memberyear)
            return jsonify(Client=result)
        else:
            return jsonify(Error="Unexpected attribute values."), 400

    def Put_Client(self, clid, client_data):
        if len(client_data) != 4:
            return jsonify(Error="Invalid Data"), 400

        daoCl = Client_Model_Dao()
        if not daoCl.Get_Client(clid):
            return jsonify(Error="Client not Found"), 404

        fname = client_data.get('fname')
        lname = client_data.get('lname')
        age = client_data.get('age')
        memberyear = client_data.get('memberyear')
        if fname and lname and age and memberyear:
            daoCl1 = Client_Model_Dao()
            client = daoCl1.Put_Client(clid, fname, lname, age, memberyear)
            result = self.Client_Build(clid, fname, lname, age, memberyear)
            return jsonify(Client=result), 202
        else:
            return jsonify(Error="Unexpected attribute values."), 400

    def Delete_Client(self, clid):
        daoCl = Client_Model_Dao()
        if not daoCl.Get_Client(clid):
            return jsonify(Error="Client not Found"), 404

        daoCl1 = Client_Model_Dao()
        result = daoCl1.Delete_Client(clid)
        if result == "Error":
            return jsonify(Error="Client is referenced"), 400
        elif result:
            return jsonify(OK="Client Deleted"), 200
        else:
            return jsonify(Error="Delete Failed"), 500
