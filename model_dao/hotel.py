# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database, DatabaseOption


# ** Class for handling database operations related to hotel model
class Hotel_Model_Dao:
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

    # ** Method to fetch all hotels from the database
    def Get_All_Hotels(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM hotel "
                 "order by hid")
        cur.execute(query)
        hotels_list = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return hotels_list

    # ** Method to fetch a specific hotel by its ID from the database
    def Get_Hotel(self, hid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM hotel "
                 "WHERE hid = %s")
        cur.execute(query, (hid,))
        hotel = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return hotel

    # ** Method to add a new hotel to the database
    def Post_Hotel(self, chid, hname, hcity):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO hotel (chid, hname, hcity) "
                 "VALUES (%s, %s, %s) "
                 "returning hid")
        cur.execute(query, (chid, hname, hcity))
        result = cur.fetchone()[0]
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return result

    # ** Method to update an existing hotel in the database
    def Put_Hotel(self, hid, chid, hname, hcity):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE hotel "
                 "SET chid = %s, hname = %s, hcity = %s "
                 "WHERE hid = %s")
        cur.execute(query, (chid, hname, hcity, hid))
        count = cur.rowcount
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return count

    # ** Method to delete an existing hotel in the database
    def Delete_Hotel(self, hid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM hotel "
                 "WHERE hid = %s")
        try:
            cur.execute(query, (hid,))
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
        
    def Get_Hotels_Chain(self, hid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = "SELECT chid FROM hotel WHERE hid = %s"
        cur.execute(query, (hid,))
        chid = cur.fetchone()[0]
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return chid
