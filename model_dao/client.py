# ** Importing Docker_Database from db module
from db import Docker_Database


# ** Class for handling database operations related to client model
class Client_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()
        
    

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all clients from the database
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

    # ** Method to fetch a specific client by its ID from the database
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

    def Post_Client(self,fname, lname, age, memberyear):
        # ** Method to add a new client to the database
        with self.db.docker_connection.cursor() as cur:
            query = ("INSERT INTO client ( fname, lname, age, memberyear)"
                     "VALUES (%s, %s, %s, %s)"
                     "returning clid")
            cur.execute(query, (fname, lname, age, memberyear))
            result = cur.fetchone()[0]
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return result
        
    def Put_Client(self, clid, fname, lname, age, memberyear):
        with self.db.docker_connection.cursor() as cur:
            query = ("UPDATE client "
                     "SET fname = %s, lname = %s, age = %s, memberyear = %s "
                     "WHERE clid = %s")
            cur.execute(query, (fname, lname, age, memberyear, clid))
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return clid
        
    def Delete_Client(self, clid):
        with self.db.docker_connection.cursor() as cur:
            query = ("DELETE FROM client "
                     "WHERE clid = %s")
            cur.execute(query, (clid,))
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return clid
        
    def Get_Client_Reservations(self, clid):
        with self.db.docker_connection.cursor() as cur:
            query = ("SELECT * "
                     "FROM reserve "
                     "WHERE clid = %s")
            cur.execute(query, (clid,))
            result = cur.fetchall()
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return result
