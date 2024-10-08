# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database, DatabaseOption


class GlobalStatistics_Model_Dao:
    def __init__(self):
        if DatabaseOption() == 'd':
            self.db = Docker_Database()
        elif DatabaseOption() == 'h':
            self.dbh = Heroku_Database()

    # * PAYMENTMETHOD
    def Get_post_PaymentMethod(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT "
                 "payment, "
                 "COUNT(reid), "
                 "ROUND(CAST(COUNT(reid)*100.0/(SELECT COUNT(reid) FROM reserve) AS numeric),2) "
                 "FROM reserve GROUP BY payment")
        cur.execute(query)
        result = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return result

    # ** TOP 3 CHAINS WITH LESS ROOMS
    def Get_Top_Three_Chains_With_Least_Rooms(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT chid, cname, COUNT(rid) as room_count "
                 "FROM chains "
                 "NATURAL INNER JOIN hotel "
                 "NATURAL INNER JOIN room "
                 "GROUP BY chid, cname "
                 "ORDER BY room_count ASC "
                 "LIMIT 3; ")
        cur.execute(query)
        result = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return result

    # ** TOP 5 HOTELS WITH MOST CAPACITY
    def Get_Top_Five_Hotels_With_Most_Capacity(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT hid, hname, sum(capacity) as total_capacity "
                 "FROM hotel "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN roomdescription "
                 "GROUP BY hid, hname "
                 "ORDER BY total_capacity DESC "
                 "LIMIT 5")
        cur.execute(query)
        result = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return result

    # HotelMethod
    def Get_top_10_hotelreservation(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("Select hid, rid,ruid,reid "
                 "from hotel natural inner join room "
                 "natural inner join roomunavailable "
                 "natural inner join reserve")
        cur.execute(query)
        result = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        return result

    def Get_top_3_monthly_reservation(self, chid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("Select reid,ruid, startdate,enddate "
                 "From reserve natural inner join roomunavailable natural inner join hotel "
                 "where chid = %s")
        cur.execute(query, (chid,))
        result = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        return result

    # * MOST_REVENUE
    def Get_post_MostRevenue(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT chid, round(cast(sum(total_cost) as numeric), 2) as total_revenue "
                 "FROM chains "
                 "NATURAL INNER JOIN hotel "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN roomunavailable "
                 "NATURAL INNER JOIN reserve "
                 "GROUP BY chid "
                 "ORDER BY total_revenue desc "
                 "limit 3")
        cur.execute(query)
        result = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return result

    # * MOST_PROFITMONTH
    def Get_post_MostProfitMonth(self):
        cur = None
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("""
                WITH monthly_reservations AS (
                SELECT
                    chains.chid,
                    EXTRACT(MONTH FROM roomunavailable.startdate) AS month, 
                    COUNT(DISTINCT reserve.reid) AS total_reservations  
                FROM roomunavailable
                JOIN reserve ON roomunavailable.ruid = reserve.ruid
                JOIN room ON roomunavailable.rid = room.rid
                JOIN hotel ON room.hid = hotel.hid
                JOIN chains ON hotel.chid = chains.chid
                GROUP BY chains.chid, month
            ),
            ranked_reservations AS (
                SELECT
                    chid,
                    month,
                    total_reservations,
                    RANK() OVER (PARTITION BY chid ORDER BY total_reservations DESC) AS rnk
                FROM monthly_reservations
            ),
            top_3_or_tied AS (
                SELECT 
                    chid, 
                    month,
                    total_reservations,
                    rnk,
                    MAX(rnk) OVER (PARTITION BY chid) AS max_rnk 
                FROM ranked_reservations
                WHERE rnk <= 3  
            ),
            final_top_3 AS (
                SELECT *,
                    ROW_NUMBER() OVER (PARTITION BY chid ORDER BY rnk, month) AS row_num
                FROM top_3_or_tied
            )
            SELECT chid, month, total_reservations
            FROM final_top_3
            WHERE row_num <= 3
            ORDER BY chid, rnk, month; 
        """)
        cur.execute(query)
        result = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return result
