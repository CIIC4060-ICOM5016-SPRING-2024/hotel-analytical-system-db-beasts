# Importing Docker_Database from db module
from db import Docker_Database


# Class for handling database operations related to client model
class Client_Model_Dao:
    def __init__(self):
        # Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to fetch all clients from the database
    def Get_All_Clients(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM client  "
                 "ORDER BY clid")
        cur.execute(query)
        client_list = cur.fetchall()
        self.db.close()
        cur.close()
        return client_list

    # Method to fetch a specific client by its ID from the database
    def Get_Client(self, clid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM client "
                 "WHERE clid = %s")
        cur.execute(query, (clid,))
        client = cur.fetchone()
        self.db.close()
        cur.close()
        return client
