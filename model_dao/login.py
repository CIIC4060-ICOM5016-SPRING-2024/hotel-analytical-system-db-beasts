# Importing Docker_Database from db module
from db import Docker_Database


# Class for handling database operations related to login model
class Login_Model_Dao:
    def __init__(self):
        # Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to fetch all logins from the database
    def Get_All_Logins(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM login "
                 "order by lid")
        cur.execute(query)
        login_list = cur.fetchall()
        self.db.close()
        cur.close()
        return login_list

    # Method to fetch a specific login by its ID from the database
    def Get_Login(self, lid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM login "
                 "WHERE lid = %s")
        cur.execute(query, (lid,))
        login = cur.fetchone()
        self.db.close()
        cur.close()
        return login
