# ** Importing Docker_Database from db module
from db import Docker_Database


class GlobalStatistics_Model_Dao:
    def __init__(self):
        self.db = Docker_Database()

    # * PAYMENTMETHOD
    def Get_post_PaymentMethod(self):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT "
                 "payment, "
                 "COUNT(reid), "
                 "ROUND(CAST(COUNT(reid)*100.0/(SELECT COUNT(reid) FROM reserve) AS numeric),2) "
                 "FROM reserve GROUP BY payment")
        cur.execute(query)
        result = cur.fetchall()
        self.db.close()
        cur.close()
        return result
