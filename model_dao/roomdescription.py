# ** Importing Docker_Database from db module
from db import Docker_Database


# ** Class for handling database operations related to RoomDescription model
class RoomDescription_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all RoomDescriptions from the database
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

    # ** Method to fetch a specific RoomDescription by its ID from the database
    def Get_RoomDescription(self, rdid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT *  "
                 "FROM roomdescription  "
                 "WHERE rdid = %s")
        cur.execute(query, (rdid,))
        roomdescription = cur.fetchone()
        self.db.close()
        cur.close()
        return roomdescription

    # ** Method to add a new RoomDescription to the database
    def Post_RoomDescription(self, rname, rtype, capacity, ishandicap):
        cur = self.db.docker_connection.cursor()
        query = ("INSERT INTO roomdescription (rname, rtype, capacity, ishandicap) "
                 "VALUES (%s, %s, %s, %s)"
                 "returning rdid")
        cur.execute(query, (rname, rtype, capacity, ishandicap))
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return result

    # ** Method to update an existing RoomDescription in the database
    def Put_RoomDescription(self, rdid, rname, rtype, capacity, ishandicap):
        cur = self.db.docker_connection.cursor()
        query = ("UPDATE roomdescription "
                 "SET rname = %s, rtype = %s, capacity = %s, ishandicap = %s "
                 "WHERE rdid = %s")
        cur.execute(query, (rname, rtype, capacity, ishandicap, rdid))
        count = cur.rowcount
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return count

    def Delete_RoomDescription(self, rdid):
        cur = self.db.docker_connection.cursor()
        query = ("DELETE FROM roomdescription "
                 "WHERE rdid = %s")
        try:
            cur.execute(query, (rdid,))
            count = cur.rowcount
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return count
        except:
            return "Error deleting"
