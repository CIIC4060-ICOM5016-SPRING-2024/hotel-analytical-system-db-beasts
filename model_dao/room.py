# Importing Docker_Database from db module
from db import Docker_Database


# Class for handling database operations related to room model
class ROOM_Model_Dao:
    def __init__(self):
        # Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to fetch all rooms from the database
    def Get_All_Rooms(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM room "
                 "ORDER BY rid")
        cur.execute(query)
        room_list = cur.fetchall()
        self.db.close()
        cur.close()
        return room_list
