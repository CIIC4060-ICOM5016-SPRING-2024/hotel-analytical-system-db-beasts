# ** Importing Docker_Database from db module
from db import Docker_Database


# ** Class for handling database operations related to reserve model
class Reserve_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all reserves from the database
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

    # ** Method to fetch a specific reserve by its ID from the database
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
    
    def Post_Reserve(self, ruid, clid, total_cost, payment, guests):
        # ** Method to add a new reserve to the database
        with self.db.docker_connection.cursor() as cur:
            query = ("INSERT INTO reserve (ruid, clid, total_cost, payment, guests)"
                    "VALUES (%s, %s, %s, %s, %s)"
                    "returning reid")
            cur.execute(query, (ruid, clid, total_cost, payment, guests))
            result = cur.fetchone()[0]
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return result
            
    def Put_Reserve(self, ruid, clid, total_cost, payment, guests,reid):
        # ** Method to update an existing reserve in the database
        cur = self.db.docker_connection.cursor()
        query = ("UPDATE reserve "
                 "SET ruid = %s, clid = %s, total_cost = %s, payment = %s, guests = %s "
                 "WHERE reid = %s")
        cur.execute(query, (ruid, clid, total_cost, payment,guests,reid))
        count = cur.rowcount
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return count
    
    
    def Delete_Reserve(self, reid):
        # ** Method to delete an existing reserve in the database
        cur = self.db.docker_connection.cursor()
        query = ("DELETE FROM reserve "
                 "WHERE reid = %s")
        cur.execute(query, (reid,))
        count = cur.rowcount
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return count