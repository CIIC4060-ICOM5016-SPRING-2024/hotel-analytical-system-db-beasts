# Importing Docker_Database from db module
from db import Docker_Database


# Class for handling database operations related to RoomDescription model
class RoomDescription_Model_Dao:
    def __init__(self):
        # Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to fetch all RoomDescriptions from the database
    def Get_All_RoomDescriptions(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM roomdescription "
                 "ORDER BY rdid")
        cur.execute(query)
        roomdescription_list = cur.fetchall()
        self.db.close()
        cur.close()
        return roomdescription_list
