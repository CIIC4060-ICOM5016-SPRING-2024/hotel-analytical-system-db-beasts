# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database


# ** Class for handling database operations related to client model
class Client_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()
        # self.dbh = Heroku_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all clients from the database
    def Get_All_Clients(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM client  "
                 "ORDER BY clid")
        cur.execute(query)
        client_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return client_list

    # ** Method to fetch a specific client by its ID from the database
    def Get_Client(self, clid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM client "
                 "WHERE clid = %s")
        cur.execute(query, (clid,))
        client = cur.fetchone()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return client

    def Post_Client(self, fname, lname, age, memberyear):
        # ** Method to add a new client to the database
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO client ( fname, lname, age, memberyear)"
                 "VALUES (%s, %s, %s, %s)"
                 "returning clid")
        cur.execute(query, (fname, lname, age, memberyear))
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    def Put_Client(self, clid, fname, lname, age, memberyear):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE client "
                 "SET fname = %s, lname = %s, age = %s, memberyear = %s "
                 "WHERE clid = %s")
        cur.execute(query, (fname, lname, age, memberyear, clid))
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return clid

    def Delete_Client(self, clid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM client "
                     "WHERE clid = %s")
        cur.execute(query, (clid,))
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return clid

    def Get_Client_Reservations(self, clid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM reserve "
                 "WHERE clid = %s")
        cur.execute(query, (clid,))
        result = cur.fetchall()
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result
