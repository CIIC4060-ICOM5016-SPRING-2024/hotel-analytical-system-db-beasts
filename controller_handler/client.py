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
    
    def Client_Build(self,clid,fname, lname, age, memberyear):
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
        return jsonify(clients=result)

    # ** Method to retrieve a specific client by its ID
    def Get_Client(self, client_id):
        dao = Client_Model_Dao()
        client = dao.Get_Client(client_id)
        if client is not None:
            result = self.Client_Dict(client)
            return jsonify(client=result)
        return jsonify("Not Found"), 404

    def Post_Client(self, client_data):
        if len(client_data) != 4:
            return jsonify(Error="Invalid Data"), 400
        fname = client_data['fname']
        lname = client_data['lname']
        age = client_data['age']
        memberyear = client_data['memberyear']
        if any(elm for elm in [fname, lname, age, memberyear] if elm is not None):
            dao = Client_Model_Dao()
            clid = dao.Post_Client(fname, lname, age, memberyear)
            client_result = self.Client_Build(clid, fname,lname, age, memberyear)
            
            return jsonify(client=client_result),201
        
        else:
            return jsonify(Error="Unexpected attribute values"), 400
        
    
    def Put_Client(self, client_id, client_data):
        if len(client_data) != 4:
            return jsonify(Error="Invalid Data"), 400
        
        if client_id is None:
            return jsonify(Error="Client ID cannot be empty"), 400
        
        client = self.Get_Client(client_id)
        
        if client is None:
            return jsonify(Error="Client not found"), 404
        
        fname = client_data['fname']
        lname = client_data['lname']
        age = client_data['age']
        memberyear = client_data['memberyear']
        
        if any(elm for elm in [fname, lname, age, memberyear] if elm is not None):
            dao = Client_Model_Dao()
            dao.Put_Client(client_id, fname, lname, age, memberyear)
            client_result = self.Client_Build(client_id, fname, lname, age, memberyear)
            
            if client_result is None:
                return jsonify(Error="Could not build client model"), 400
            
            return jsonify(client=client_result), 200
        
        else:
            return jsonify(Error="Unexpected attribute values"), 400
    
    def Delete_Client(self, client_id):
        if client_id is None:
            return jsonify(Error="Client ID cannot be empty"), 400
        
        clientdao = Client_Model_Dao()
        client = clientdao.Get_Client(client_id)
        if client is not None:
            
            #Checking if client has reservations on system
            clientdao2 = Client_Model_Dao()
            client_reservations = clientdao2.Get_Client_Reservations(client_id)

            if len(client_reservations) == 0:
                
                dao = Client_Model_Dao()
                result = dao.Delete_Client(client_id)
                
                if result:
                    return jsonify("Deleted"), 200
            else:
                return jsonify(Error="Client has reservations, delete reservations to delete client"), 400

        else:
            return jsonify(Error="Client not found"), 404
