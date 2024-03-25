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
