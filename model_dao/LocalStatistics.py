# ** Importing Docker_Database from db module
from db import Docker_Database


class LocalStatistics_Model_Dao:
    def __init__(self):
        self.db = Docker_Database()

    # * ROOMTYPE
    def Get_post_RoomType(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT hid as hotel, rtype as room_type, count(reid) as total_reserves "
                 "FROM reserve "
                 "natural inner join roomunavailable "
                 "natural inner join room "
                 "natural inner join roomdescription "
                 "where hid = %s "
                 "group by  rtype, hid")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        cur.close()
        return result_list

    # * MOSTCREDITCARD
    def Get_post_MostCreditCard(self, hid):
        cur = self.db.docker_connection.cursor()
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
        cur.close()
        return result_list

    # * HANDICAPROOM
    def Get_post_HandicapRoom(self, hid):
        cur = self.db.docker_connection.cursor()
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
        cur.close()
        return result_list

    # * LEASTRESERVE
    def Get_post_LeastReserve(self, hid):
        cur = self.db.docker_connection.cursor()
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
        cur.close()
        return result_list

    # * LEASTGUESTS
    def Get_post_LeastGuests(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("select hid, rid, rname, rtype, "
                 "guests || ':' || capacity as guest_capacity, "
                 "round(abs((guests::float/capacity::float)::numeric - 1) ,2) as space "
                 "from room "
                 "natural inner join roomdescription "
                 "natural inner join roomunavailable "
                 "natural inner join reserve "
                 "natural inner join hotel "
                 "where hid = %s "
                 "group by hid, rid, rname, rtype, guest_capacity, space "
                 "order by space asc "
                 "limit 3")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        cur.close()
        return result_list

    # * HIGHESTPAID
    def Get_post_HighestPaid(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("select hid, eid, fname || ' ' || lname as fullname, position, salary "
                 "from employee "
                 "natural inner join hotel "
                 "where position = 'Regular' and hid = %s "
                 "order by salary desc "
                 "limit 3;")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        cur.close()
        return result_list
