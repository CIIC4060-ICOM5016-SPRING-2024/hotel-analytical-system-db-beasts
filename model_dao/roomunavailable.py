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

    def Post_RoomUnavailable(self, rid, startdate, enddate):
        cur = self.db.docker_connection.cursor()
        
        tempquery1 = "SELECT MAX(ruid) FROM roomunavailable"
        cur.execute(tempquery1)
        ruid = cur.fetchone()[0]
        
        #Change to query after testing
        query = """
            INSERT INTO roomunavailable (rid, startdate, enddate)
            VALUES (%s, %s, %s)
            returning ruid
        """
        
        querytemp = """
            Alter sequence roomunavailable_ruid_seq restart with %s;
        
            INSERT INTO roomunavailable (rid, startdate, enddate)
            VALUES (%s, %s, %s)
            returning ruid
        """
        
        print(ruid+1,rid, startdate, enddate)
        #Change to query after testing
        #cur.execute(query, (rid, startdate, enddate))
        cur.execute(querytemp, (ruid+1,rid, startdate, enddate))  # Pass values as parameters
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return result
    
    def Put_RoomUnavailable(self, ruid, rid,startdate, enddate):
        cur = self.db.docker_connection.cursor()
        query = """
            UPDATE roomunavailable
            SET startdate = %s, rid = %s, enddate = %s
            WHERE ruid = %s
        """
        cur.execute(query, (startdate, rid,enddate, ruid))
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()

    def Delete_RoomUnavailable(self, ruid):
        cur = self.db.docker_connection.cursor()
        query = ("DELETE FROM roomunavailable "
                 "WHERE ruid = %s")
        cur.execute(query, (ruid,))
        count = cur.rowcount
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return count