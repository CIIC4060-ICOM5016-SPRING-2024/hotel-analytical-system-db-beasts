# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database


# ** Class for handling database operations related to room model
class Room_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()
        # self.dbh = Heroku_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all rooms from the database
    def Get_All_Rooms(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM room "
                 "ORDER BY rid")
        cur.execute(query)
        room_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return room_list

    # ** Method to fetch a specific room by its ID from the database
    def Get_Room(self, rid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM room "
                 "WHERE rid = %s")
        cur.execute(query, (rid,))
        room = cur.fetchone()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return room

    # ** Method to add a new room to the database
    def Post_Room(self, hid, rdid, rprice):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO room (hid, rdid, rprice) "
                 "VALUES (%s, %s, %s)"
                 "returning rid")
        cur.execute(query, (hid, rdid, rprice))
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    # ** Method to update an existing room in the database
    def Put_Room(self, rid, hid, rdid, rprice):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE room "
                 "SET hid = %s, rdid = %s, rprice = %s "
                 "WHERE rid = %s")
        cur.execute(query, (hid, rdid, rprice, rid))
        count = cur.rowcount
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return count

    # ** Method to delete an existing room in the database
    def Delete_Room(self, rid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM room "
                 "WHERE rid = %s")
        try:
            cur.execute(query, (rid,))
            count = cur.rowcount
            self.db.docker_connection.commit()
            # self.dbh.heroku_connection.commit()
            self.db.close()
            # self.dbh.close()
            cur.close()
            return count
        except:
            self.db.close()
            # self.dbh.close()
            cur.close()
            return "Error deleting"

    """
    ------------------
    * TOOL OPERATIONS
    ------------------
    """

    # ** Looking for room information based on the supposed hotel.
    def Get_Room_Info(self, rid, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("select rid, hid, rdid, capacity, rprice "
                 "from room "
                 "natural inner join roomdescription "
                 "where rid = %s and hid = %s")
        cur.execute(query, (rid, hid,))
        room_info = cur.fetchone()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return room_info
