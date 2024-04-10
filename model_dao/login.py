# ** Importing Docker_Database from db module
from db import Docker_Database


# ** Class for handling database operations related to login model
class Login_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all logins from the database
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

    # ** Method to fetch a specific login by its ID from the database
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

        # ** Method to add a new employee to the database
    def Post_Login(self, eid, username, password):
        cur = self.db.docker_connection.cursor()
        query = ("INSERT INTO login (eid, username, password)"
                 "VALUES (%s, %s, %s)"
                 "returning lid")
        try:
            cur.execute(query, (eid, username, password))
            result = cur.fetchone()[0]
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return result
        except:
            return "Error"

    def Put_Login(self, lid, username, password):
        cur = self.db.docker_connection.cursor()
        query = ("UPDATE login "
                 "SET username = %s, password = %s "
                 "WHERE lid = %s")
        try:
            cur.execute(query, (username, password, lid))
            count = cur.rowcount
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return count
        except:
            return "Error"

    def Delete_Login(self, lid):
        cur = self.db.docker_connection.cursor()
        query = ("DELETE FROM login "
                 "WHERE lid = %s")
        try:
            cur.execute(query, (lid,))
            count = cur.rowcount
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return count
        except:
            return "We couldn't delete your information, sorry!"

    """

       ------------------
       * TOOLS OPERATIONS 
       ------------------

    """

    def Get_ID_Login(self, eid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT lid "
                 "FROM login "
                 "WHERE eid = %s")
        cur.execute(query, (eid,))
        login = cur.fetchone()
        self.db.close()
        cur.close()
        return login
