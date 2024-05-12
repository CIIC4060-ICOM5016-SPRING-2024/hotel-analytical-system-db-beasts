# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database


class GlobalStatistics_Model_Dao:
    def __init__(self):
        self.db = Docker_Database()
        # self.dbh = Heroku_Database()

    # * PAYMENTMETHOD
    def Get_post_PaymentMethod(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT "
                 "payment, "
                 "COUNT(reid), "
                 "ROUND(CAST(COUNT(reid)*100.0/(SELECT COUNT(reid) FROM reserve) AS numeric),2) as percentage "
                 "FROM reserve GROUP BY payment "
                 "ORDER BY percentage")
        cur.execute(query)
        result = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    # * MOST_REVENUE
    def Get_post_MostRevenue(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT chid, cname, round(cast(sum(total_cost) as numeric), 2) as total_revenue "
                 "FROM chains "
                 "NATURAL INNER JOIN hotel "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN roomunavailable "
                 "NATURAL INNER JOIN reserve "
                 "GROUP BY chid, cname "
                 "ORDER BY total_revenue desc "
                 "limit 3")
        cur.execute(query)
        result = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    # * LEAST_ROOMS
    def Get_post_LeastRooms(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT chid, cname, count(rid) as total_rooms "
                 "FROM chains "
                 "NATURAL INNER JOIN hotel "
                 "NATURAL INNER JOIN room "
                 "GROUP BY chid, cname "
                 "ORDER BY total_rooms asc "
                 "LIMIT 3")
        cur.execute(query)
        result = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    # * MOST_CAPACITY
    def Get_post_MostCapacity(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT hid, hname, sum(capacity) as total_capacity "
                 "FROM hotel "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN roomdescription "
                 "GROUP BY hid, hname "
                 "ORDER BY total_capacity desc "
                 "LIMIT 5")
        cur.execute(query)
        result = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    # * MOST_RESERVATION
    def Get_post_MostReservation(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT hid, hname, count(reid) as total_reserves "
                 "FROM hotel "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN roomunavailable "
                 "NATURAL INNER JOIN reserve "
                 "GROUP BY hid, hname "
                 "ORDER BY total_reserves desc "
                 "limit (SELECT ceil(0.1 * (SELECT count(hid)-1 "
                 "       FROM hotel)))")
        cur.execute(query)
        result = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result

    # * MOST_PROFITMONTH
    def Get_post_MostProfitMonth(self):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("""
                    WITH month_reservations AS (
                        SELECT
                            chid,
                            EXTRACT(MONTH FROM startdate::date) AS month,
                            COUNT(reid) AS total_reservations,
                            RANK() OVER (PARTITION BY chid ORDER BY COUNT(reid) DESC) AS ranks
                        FROM
                            reserve
                        NATURAL INNER JOIN
                            roomunavailable
                        NATURAL INNER JOIN
                            room
                        NATURAL INNER JOIN
                            hotel
                        GROUP BY
                            chid, month
                    ),
                    top_3_or_tied AS (
                                    SELECT
                                        chid,
                                        month,
                                        total_reservations,
                                        ranks,
                                        MAX(ranks) OVER (PARTITION BY chid) AS max_rnk
                                    FROM month_reservations
                                    WHERE ranks <= 3  -- Filter here to avoid unnecessary calculations
                                ),
                    final_top_3 AS (
                                    SELECT *,
                                        ROW_NUMBER() OVER (PARTITION BY chid ORDER BY ranks, month) AS row_num
                                    FROM top_3_or_tied
                                )
                    SELECT
                        chid,
                        month,
                        total_reservations,
                        ranks
                    FROM
                        final_top_3
                    WHERE
                        row_num <= 3
                    ORDER BY
                        chid, total_reservations desc, month;
        """)
        cur.execute(query)
        result = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result
