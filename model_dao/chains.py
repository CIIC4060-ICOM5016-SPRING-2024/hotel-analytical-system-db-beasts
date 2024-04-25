# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database


# ** Class for handling database operations related to chains model
class Chains_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        self.db = Docker_Database()
        # self.dbh = Heroku_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all chains from the database
    def Get_All_Chains(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM chains "
                 "order by chid")
        cur.execute(query)
        chains_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return chains_list

    # ** Method to fetch a specific chain by its ID from the database
    def Get_Chain(self, chid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM chains "
                 "WHERE chid = %s")
        cur.execute(query, (chid,))
        chain = cur.fetchone()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return chain

    # ** Method to add a new chain to the database
    def Post_Chain(self, cname, springmkup, summermkup, fallmkup, wintermkup):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO chains (cname, springmkup, summermkup, fallmkup, wintermkup) "
                 "VALUES (%s, %s, %s, %s, %s) "
                 "returning chid")
        cur.execute(query, (cname, springmkup, summermkup, fallmkup, wintermkup))
        result = cur.fetchone()[0]
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    # ** Method to update an existing chain in the database
    def Put_Chain(self, chid, cname, springmkup, summermkup, fallmkup, wintermkup):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE chains "
                 "SET cname = %s, springmkup = %s, summermkup = %s, fallmkup = %s, wintermkup = %s "
                 "WHERE chid = %s")
        cur.execute(query, (cname, springmkup, summermkup, fallmkup, wintermkup, chid))
        count = cur.rowcount
        self.db.docker_connection.commit()
        # self.dbh.heroku_connection.commit()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return count

    def Delete_Chain(self, chid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM chains "
                 "WHERE chid = %s")
        try:
            cur.execute(query, (chid,))
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

    def Get_Markup(self, chid):
        """
        Retrieves the markup values for the specified chain ID from the database.

        Parameters:
            chid (int): The chain ID for which the markup values are to be retrieved.

        Returns:
            tuple: A tuple containing the markup values for spring, summer, fall, and winter.
        """

        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("""SELECT springmkup, summermkup, fallmkup, wintermkup 
                FROM chains
                WHERE chid = %s""")

        cur.execute(query, (chid,))
        markups = cur.fetchone()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return markups
