# ** Importing Docker_Database from db module
from db import Docker_Database


# ** Class for handling database operations related to chains model
class Chains_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all chains from the database
    def Get_All_Chains(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM chains "
                 "order by chid")
        cur.execute(query)
        chains_list = cur.fetchall()
        self.db.close()
        cur.close()
        return chains_list

    # ** Method to fetch a specific chain by its ID from the database
    def Get_Chain(self, chid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT * "
                 "FROM chains "
                 "WHERE chid = %s")
        cur.execute(query, (chid,))
        chain = cur.fetchone()
        self.db.close()
        cur.close()
        return chain

    # ** Method to add a new chain to the database
    def Post_Chain(self, cname, springmkup, summermkup, fallmkup, wintermkup):
        cur = self.db.docker_connection.cursor()
        query = ("INSERT INTO chains (cname, springmkup, summermkup, fallmkup, wintermkup) "
                 "VALUES (%s, %s, %s, %s, %s) "
                 "returning chid")
        cur.execute(query, (cname, springmkup, summermkup, fallmkup, wintermkup))
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return result

    # ** Method to update an existing chain in the database
    def Put_Chain(self, chid, cname, springmkup, summermkup, fallmkup, wintermkup):
        cur = self.db.docker_connection.cursor()
        query = ("UPDATE chains "
                 "SET cname = %s, springmkup = %s, summermkup = %s, fallmkup = %s, wintermkup = %s "
                 "WHERE chid = %s")
        cur.execute(query, (cname, springmkup, summermkup, fallmkup, wintermkup, chid))
        count = cur.rowcount
        self.db.docker_connection.commit()
        self.db.close()
        cur.close()
        return count

    # def Delete_Chain(self, chid):
    #     cur = self.db.docker_connection.cursor()
    #     query = ("DELETE FROM chains "
    #              "WHERE chid = %s")
    #     try:
    #         cur.execute(query, (chid,))
    #         count = cur.rowcount
    #         self.db.docker_connection.commit()
    #         self.db.close()
    #         cur.close()
    #         return count
    #     except:
    #         return "Error deleting"
