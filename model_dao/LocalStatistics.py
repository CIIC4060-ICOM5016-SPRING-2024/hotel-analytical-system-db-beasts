# ** Importing Docker_Database from db module
from db import Docker_Database, Heroku_Database


class LocalStatistics_Model_Dao:
    def __init__(self):
        #self.db = Docker_Database()
        self.dbh = Heroku_Database()

    # * ROOMTYPE
    def Get_post_RoomType(self, hid):
        # #cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT hid as hotel, rtype as room_type, count(reid) as total_reserves "
                 "FROM reserve "
                 "natural inner join roomunavailable "
                 "natural inner join room "
                 "natural inner join roomdescription "
                 "where hid = %s "
                 "group by  rtype, hid")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        # self.db.close()
        self.dbh.close()
        cur.close()
        return result_list

    # * Hotel
    def Get_handicap_rooms(self, hid):
        #cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
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
        #self.dbh.close()
        cur.close()
        return result_list

    def Get_room_availability_by_hotel(self, hid):
        #cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = ("""Select hid,chid,rid,startdate, enddate
                 From roomunavailable natural inner join room
                 natural inner join hotel
                 where hid = %s
                 Group by hid,chid,rid,startdate,enddate""")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        #self.db.close()
        self.dbh.close()
        cur.close()
        return result_list
    
    

    # * THE TOP 3 HIGHEST PAID EMPLOYEES
    def Get_post_Highest_Paid_Regular_Employees(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT hid, eid, fname, lname, salary, position "
                 "FROM employee "
                 "WHERE position = 'Regular' and hid = %s "
                 "ORDER BY salary DESC "
                 "LIMIT  3; ")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        cur.close()
        return result_list

    # * THE TOP 5 MOST DISCOUNTS HOLDER CLIENTS
    # def Get_post_Most_Discount_Clients(self, hid):
    def Get_post_MostDiscount(self, hid):
        cur = self.db.docker_connection.cursor()
        query = ("SELECT hid, clid, fname, lname, memberyear, calculate_most_discount(memberyear) as discount "
                 "FROM client "
                 "NATURAL INNER JOIN reserve "
                 "NATURAL INNER JOIN roomunavailable "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN hotel "
                 "WHERE hid = %s "
                 "ORDER BY discount DESC "
                 "LIMIT  5; ")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        self.db.close()
        cur.close()
        return result_list
