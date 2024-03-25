# Importing Docker_Database from db module
from db import Docker_Database


# Class for handling database operations related to roomunavailable model
class RoomUnavailable_Model_Dao:
    def __init__(self):
        # Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to fetch all roomsunavailable from the database
    def Get_All_RoomsUnavailable(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM roomunavailable "
                 "ORDER BY ruid")
        cur.execute(query)
        roomsunavailable_list = cur.fetchall()
        self.db.close()
        cur.close()
        return roomsunavailable_list

    # Method to fetch a specific roomunavailable by its ID from the database
    def Get_RoomUnavailable(self, ruid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM roomunavailable "
                 "WHERE ruid = %s")
        cur.execute(query, (ruid,))
        roomunavailable = cur.fetchone()
        self.db.close()
        cur.close()
        return roomunavailable
