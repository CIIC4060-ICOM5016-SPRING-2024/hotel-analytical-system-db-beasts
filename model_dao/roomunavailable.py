# ** Importing Docker_Database from db module
from db import Docker_Database


# ** Class for handling database operations related to roomunavailable model
class RoomUnavailable_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all roomsunavailable from the database
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

    # ** Method to fetch a specific roomunavailable by its ID from the database
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

    def Post_RoomUnavailable(self, rid, startdate, enddate):
        cur = self.db.docker_connection.cursor()
        query = ("INSERT INTO roomunavailable (rid, startdate, enddate) "
                 "VALUES (%s, %s, %s)"
                 "returning ruid")
        cur.execute(query, (rid, startdate, enddate))
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return result

    def Put_RoomUnavailable(self, ruid, rid, startdate, enddate):
        cur = self.db.docker_connection.cursor()
        query = ("UPDATE roomunavailable "
                 "SET rid = %s, startdate = %s, enddate = %s "
                 "WHERE ruid = %s")
        cur.execute(query, (rid, startdate, enddate, ruid))
        count = cur.rowcount
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return count

    def Delete_RoomUnavailable(self, ruid):
        cur = self.db.docker_connection.cursor()
        query = ("DELETE FROM roomunavailable "
                 "WHERE ruid = %s")
        try:
            cur.execute(query, (ruid,))
            count = cur.rowcount
            self.db.docker_connection.commit()
            self.db.close()
            cur.close()
            return count
        except:
            return "Error deleting"

    """
    ------------------
    * TOOL OPERATIONS
    ------------------
    """

    # ** Searching for the last date where the room is not available
    def RoomUnavailable_Time(self, rid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT max(enddate) as enddate "
                 "FROM roomunavailable "
                 "where rid = %s")
        cur.execute(query, (rid,))
        roomunavailable_time = cur.fetchone()
        self.db.close()
        cur.close()
        return roomunavailable_time

    def RoomUnavailable_Time_put(self, rid, ruid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT max(enddate) as enddate "
                 "FROM roomunavailable "
                 "WHERE rid = %s and ruid != %s")
        cur.execute(query, (rid, ruid))
        roomunavailable_time = cur.fetchone()
        self.db.close()
        cur.close()
        return roomunavailable_time

    def Get_Roomdateavailable(self, rid):
            cur = self.db.docker_connection.cursor()
            query = """
            SELECT MAX(enddate) AS max_enddate 
            FROM roomunavailable 
            WHERE rid = %s
        """
            cur.execute(query, (rid,))
            room_info = cur.fetchone()
            cur.close()  # Close the cursor after fetching the result
            return room_info