# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database, DatabaseOption


# ** Class for handling database operations related to room model
class Room_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        if DatabaseOption() == 'd':
            self.db = Docker_Database()
        elif DatabaseOption() == 'h':
            self.dbh = Heroku_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all rooms from the database
    def Get_All_Rooms(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM room "
                 "ORDER BY rid")
        cur.execute(query)
        room_list = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return room_list

    # ** Method to fetch a specific room by its ID from the database
    def Get_Room(self, rid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM room "
                 "WHERE rid = %s")
        cur.execute(query, (rid,))
        room = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return room

    # ** Method to add a new room to the database
    def Post_Room(self, hid, rdid, rprice):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO room (hid, rdid, rprice) "
                 "VALUES (%s, %s, %s)"
                 "returning rid")
        cur.execute(query, (hid, rdid, rprice))
        result = cur.fetchone()[0]
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return result

    # ** Method to update an existing room in the database
    def Put_Room(self, rid, hid, rdid, rprice):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE room "
                 "SET hid = %s, rdid = %s, rprice = %s "
                 "WHERE rid = %s")
        cur.execute(query, (hid, rdid, rprice, rid))
        count = cur.rowcount
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return count

    # ** Method to delete an existing room in the database
    def Delete_Room(self, rid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM room "
                 "WHERE rid = %s")
        try:
            cur.execute(query, (rid,))
            count = cur.rowcount
            if DatabaseOption() == 'd':
                self.db.docker_connection.commit()
                self.db.close()
            elif DatabaseOption() == 'h':
                self.dbh.heroku_connection.commit()
                self.dbh.close()
            cur.close()
            return count
        except:
            if DatabaseOption() == 'd':
                self.db.close()
            elif DatabaseOption() == 'h':
                self.dbh.close()
            cur.close()
            return "Error deleting"

    """
    ------------------
    * TOOL OPERATIONS
    ------------------
    """

    # ** Looking for room information based on the supposed hotel.
    def Get_Room_Info(self, rid, hid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("select rid, hid, rdid, capacity, rprice "
                 "from room "
                 "natural inner join roomdescription "
                 "where rid = %s and hid = %s")
        cur.execute(query, (rid, hid,))
        room_info = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return room_info

    def reserve_Get_Room_info(self, room_id):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT rid, hid, rdid, capacity ,rprice "
                 "FROM room "
                 "NATURAL INNER JOIN roomdescription "
                 "WHERE rid = %s ")
        cur.execute(query, (room_id,))
        room_info = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return room_info
