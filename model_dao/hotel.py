# ** Importing Docker_Database from db module
from db import Docker_Database


# ** Class for handling database operations related to hotel model
class Hotel_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all hotels from the database
    def Get_All_Hotels(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM hotel "
                 "order by hid")
        cur.execute(query)
        hotels_list = cur.fetchall()
        self.db.close()
        cur.close()
        return hotels_list

    # ** Method to fetch a specific hotel by its ID from the database
    def Get_Hotel(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM hotel "
                 "WHERE hid = %s")
        cur.execute(query, (hid,))
        hotel = cur.fetchone()
        self.db.close()
        cur.close()
        return hotel

    # ** Method to add a new hotel to the database
    def Post_Hotel(self, chid, hname, hcity):
        cur = self.db.docker_connection.cursor()
        query = ("INSERT INTO hotel (chid, hname, hcity) "
                 "VALUES (%s, %s, %s) "
                 "returning hid")
        cur.execute(query, (chid, hname, hcity))
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        self.db.close()
        return result

    # ** Method to update an existing hotel in the database
    def Put_Hotel(self, hid, chid, hname, hcity):
        cur = self.db.docker_connection.cursor()
        query = ("UPDATE hotel "
                 "SET chid = %s, hname = %s, hcity = %s "
                 "WHERE hid = %s")
        cur.execute(query, (chid, hname, hcity, hid))
        count = cur.rowcount
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return count

    # ** Method to delete an existing hotel in the database
    def Delete_Hotel(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("DELETE FROM hotel "
                 "WHERE hid = %s")
        try:
            cur.execute(query, (hid,))
            count = cur.rowcount
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return count
        except:
            return "Error deleting"
        
    def Get_Hotels_Chain(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("""SELECT chid FROM hotel WHERE hid = %s""")
        cur.execute(query, (hid,))
        chid = cur.fetchone()[0]
        self.db.close()
        cur.close()
        return chid
