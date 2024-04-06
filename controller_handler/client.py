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
