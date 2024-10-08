# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database, DatabaseOption


# ** Class for handling database operations related to roomunavailable model
class RoomUnavailable_Model_Dao:
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

    # ** Method to fetch all roomsunavailable from the database
    def Get_All_RoomsUnavailable(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM roomunavailable "
                 "ORDER BY ruid")
        cur.execute(query)
        roomsunavailable_list = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return roomsunavailable_list

    # ** Method to fetch a specific roomunavailable by its ID from the database
    def Get_RoomUnavailable(self, ruid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM roomunavailable "
                 "WHERE ruid = %s")
        cur.execute(query, (ruid,))
        roomunavailable = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return roomunavailable

    def Post_RoomUnavailable(self, rid, startdate, enddate):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO roomunavailable (rid, startdate, enddate) "
                 "VALUES (%s, %s, %s)"
                 "returning ruid")
        cur.execute(query, (rid, startdate, enddate))
        result = cur.fetchone()[0]
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return result

    def Put_RoomUnavailable(self, ruid, rid, startdate, enddate):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE roomunavailable "
                 "SET rid = %s, startdate = %s, enddate = %s "
                 "WHERE ruid = %s")
        cur.execute(query, (rid, startdate, enddate, ruid))
        count = cur.rowcount
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return count

    def Delete_RoomUnavailable(self, ruid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM roomunavailable "
                 "WHERE ruid = %s")
        try:
            cur.execute(query, (ruid,))
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

    # ** Searching for the last date where the room is not available
    def RoomUnavailable_Time(self, rid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT max(enddate) as enddate "
                 "FROM roomunavailable "
                 "where rid = %s")
        cur.execute(query, (rid,))
        roomunavailable_time = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return roomunavailable_time

    def RoomUnavailable_Time_put(self, rid, ruid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT max(enddate) as enddate "
                 "FROM roomunavailable "
                 "WHERE rid = %s and ruid != %s")
        cur.execute(query, (rid, ruid))
        roomunavailable_time = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return roomunavailable_time

    def Get_Roomdateavailable(self, rid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT MAX(enddate) AS max_enddate "
                 "FROM roomunavailable "
                 "WHERE rid = %s")
        cur.execute(query, (rid,))
        room_info = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return room_info
