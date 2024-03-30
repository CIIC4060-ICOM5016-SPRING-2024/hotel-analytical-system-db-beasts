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
