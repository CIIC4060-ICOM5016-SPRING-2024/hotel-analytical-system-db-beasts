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
    def Get_post_top5_HandicapRoom_Reg(self, hid):
        # #cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = (
            "SELECT hid as hotel, rid as roomID ,rtype as room_type, count(reid) as total_reserve, ishandicap as "
            "handicap_room "
            "FROM reserve "
            "natural inner join roomunavailable "
            "natural inner join room "
            "natural inner join roomdescription "
            "where hid = %s and ishandicap = true "
            "group by hid,rid, rtype, ishandicap "
            "order by total_reserve desc")
        cur.execute(query, (hid,))
        result_list = cur.fetchall()
        # self.db.close()
        self.dbh.close()
        cur.close()
        return result_list

    def Get_post_top5_HandicapRoom_Sup(self, hid):
        #cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()

        chidquery = "SELECT chid FROM hotel WHERE hid = %s"
        cur.execute(chidquery, (hid,))
        chid = cur.fetchone()[0]
        query = (
            "SELECT hid as hotel, rid as roomID ,rtype as room_type, count(reid) as total_reserve, ishandicap as "
            "handicap_room "
            "FROM reserve "
            "natural inner join roomunavailable "
            "natural inner join room "
            "natural inner join roomdescription "
            "natural inner join hotel "
            "where ishandicap = true and chid = %s "
            "group by hid,rid, rtype, ishandicap "
            "order by total_reserve desc")
        cur.execute(query, (chid,))
        result_list = cur.fetchall()
        #self.db.close()
        self.dbh.close()
        cur.close()
        return result_list

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
    
    
