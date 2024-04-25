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
        # self.dbh.close()
        cur.close()
        return result_list

    # * Hotel
    def Get_handicap_rooms(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = (
            "SELECT hid,chid,rid,reid,ishandicap as handicap_room "
            "FROM reserve "
            "natural inner join roomunavailable "
            "natural inner join room "
            "natural inner join roomdescription "
            "natural inner join hotel "
            "where ishandicap = true and hid = %s "
            "group by hid,chid,rid,reid,ishandicap ")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    def Get_room_availability_by_hotel(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("""Select hid,chid,rid,startdate, enddate
                 From roomunavailable natural inner join room
                 natural inner join hotel
                 where hid = %s
                 Group by hid,chid,rid,startdate,enddate""")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * THE TOP 3 HIGHEST PAID EMPLOYEES
    def Get_post_Highest_Paid_Regular_Employees(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT hid, eid, fname, lname, salary, position "
                 "FROM employee "
                 "WHERE position = 'Regular' and hid = %s "
                 "ORDER BY salary DESC "
                 "LIMIT  3; ")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        # self.dbh.close()
        cur.close()
        return result_list

    # * THE TOP 5 MOST DISCOUNTS HOLDER CLIENTS
    # def Get_post_Most_Discount_Clients(self, hid):
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

    # * LEASTGUESTS
    def Get_post_LeastGuests(self, hid):
        cur = self.db.docker_connection.cursor()
        # cur = self.dbh.heroku_connection.cursor()
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
        # self.dbh.close()
        cur.close()
        return result_list

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
