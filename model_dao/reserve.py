# Importing Docker_Database from db module
from db import Docker_Database


# Class for handling database operations related to reserve model
class Reserve_Model_Dao:
    def __init__(self):
        # Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # Method to fetch all reserves from the database
    def Get_All_Reserves(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM reserve  "
                 "ORDER BY reid")
        cur.execute(query)
        reserve_list = cur.fetchall()
        self.db.close()
        cur.close()
        return reserve_list

    # Method to fetch a specific reserve by its ID from the database
    def Get_Reserve(self, reid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM reserve "
                 "WHERE reid = %s")
        cur.execute(query, (reid,))
        reserve = cur.fetchone()
        self.db.close()
        cur.close()
        return reserve
