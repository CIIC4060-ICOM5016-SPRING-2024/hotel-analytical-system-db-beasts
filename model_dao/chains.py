from db import Docker_Database  # , Heroku_Database


class Chains_Model_Dao:
    def __init__(self):
        self.db = Docker_Database()
        # self.db = Heroku_Database()

    def Get_All_Chains(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.db.heroku_connection.cursor()
        query = "SELECT * FROM chains order by chid"
        cur.execute(query)
        chains_list = cur.fetchall()
        self.db.close()
        cur.close()
        return chains_list

    def Get_Chain(self, chid):
        cur = self.db.docker_connection.cursor()
        # cur = self.db.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM chains "
                 "WHERE chid = %s")
        cur.execute(query, (chid,))
        chain = cur.fetchone()
        self.db.close()
        cur.close()
        return chain

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
