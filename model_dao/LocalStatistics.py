# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database


class LocalStatistics_Model_Dao:
    def __init__(self):
        self.db = Docker_Database()
        # self.dbh = Heroku_Database()

    # * ROOMTYPE
    def Get_post_RoomType(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT hid, rtype as room_type, count(reid) as total_reserves "
                 "FROM reserve "
                 "natural inner join roomunavailable "
                 "natural inner join room "
                 "natural inner join roomdescription "
                 "natural inner join hotel "
                 "where hid = %s "
                 "group by  rtype, hid "
                 "ORDER BY total_reserves")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * MOSTCREDITCARD
    def Get_post_MostCreditCard(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT clid, age, hid, chid, payment, count(reid) as total_reserves "
                 "FROM client "
                 "NATURAL INNER JOIN reserve "
                 "NATURAL INNER JOIN roomunavailable "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN hotel "
                 "WHERE age < 30 and payment = 'credit card' and hid = %s "
                 "GROUP BY clid, age, payment, hid, chid "
                 "ORDER BY total_reserves desc limit 5")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * HANDICAPROOM
    def Get_post_HandicapRoom(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("select hid, rid, rname, rtype, ishandicap, count(reid) as total_reserves "
                 "from reserve "
                 "natural inner join roomunavailable "
                 "natural inner join room "
                 "natural inner join roomdescription "
                 "natural inner join hotel "
                 "where ishandicap = true and hid = %s "
                 "group by ishandicap, rtype, rname, rid, hid "
                 "order by total_reserves desc "
                 "limit 5; ")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * LEASTRESERVE
    def Get_post_LeastReserve(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("select hid, rid, rname, rtype, sum(enddate-startdate) as unavailable "
                 "from room "
                 "natural inner join roomunavailable "
                 "natural inner join roomdescription "
                 "natural inner join hotel "
                 "where hid = %s "
                 "group by rid, rname, rtype, hid "
                 "order by unavailable asc "
                 "limit 3; ")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * LEASTGUESTS
    def Get_post_LeastGuests(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("select hid, rid, rname || ' ' || rtype as room, "
                 "round((avg(guests::float)/capacity)::numeric, 2) as ratio "
                 "from room "
                 "natural inner join roomdescription "
                 "natural inner join roomunavailable "
                 "natural inner join reserve "
                 "natural inner join hotel "
                 "natural inner join chains "
                 "where hid = %s "
                 "group by hid, rid, room, capacity "
                 "order by ratio asc "
                 "limit 3")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * HIGHESTPAID
    def Get_post_HighestPaid(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("select hid, eid, fname || ' ' || lname as fullname, position, salary "
                 "from employee "
                 "natural inner join hotel "
                 "where position = 'Regular' and hid = %s "
                 "order by salary desc "
                 "limit 3;")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * MOSTDISCOUNT
    def Get_post_MostDiscount(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT hid, clid, fname, lname, memberyear, "
                 "discount_percentage(memberyear) as discount_percentage, "
                 "sum(total_cost) as all_payments, "
                 "round(((sum(total_cost))/(1-discount_percentage(memberyear)))::numeric,2) as not_discount, "
                 "round(((sum(total_cost))/(1-discount_percentage(memberyear)) - sum(total_cost))::numeric,2) "
                 "as discount "
                 "FROM client "
                 "NATURAL INNER JOIN reserve "
                 "NATURAL INNER JOIN roomunavailable "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN hotel "
                 "WHERE hid = %s "
                 "group by memberyear, lname, fname, clid, hid "
                 "ORDER BY discount DESC "
                 "LIMIT  5;")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list
