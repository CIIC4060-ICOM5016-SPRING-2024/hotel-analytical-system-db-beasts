# ** Importing Docker_Database from db module
from config.db import Docker_Database, Heroku_Database, DatabaseOption
import datetime


# ** Class for handling database operations related to reserve model
class Reserve_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        if DatabaseOption() == 'd':
            self.db = Docker_Database()
        elif DatabaseOption() == 'h':
            self.dbh = Heroku_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all reserves from the database
    def Get_All_Reserves(self):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM reserve  "
                 "ORDER BY reid")
        cur.execute(query)
        reserve_list = cur.fetchall()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return reserve_list

    # ** Method to fetch a specific reserve by its ID from the database
    def Get_Reserve(self, reid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM reserve "
                 "WHERE reid = %s")
        cur.execute(query, (reid,))
        reserve = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return reserve

    def Post_Reserve(self, ruid, clid, total_cost, payment, guests):
        # ** Method to add a new reserve to the database
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO reserve (ruid, clid, total_cost, payment, guests)"
                 "VALUES (%s, %s, %s, %s, %s)"
                 "returning reid")
        cur.execute(query, (ruid, clid, total_cost, payment, guests))
        result = cur.fetchone()[0]
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return result

    def Put_Reserve(self, ruid, clid, total_cost, payment, guests, reid):
        # ** Method to update an existing reserve in the database
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE reserve "
                 "SET ruid = %s, clid = %s, total_cost = %s, payment = %s, guests = %s "
                 "WHERE reid = %s")
        cur.execute(query, (ruid, clid, total_cost, payment, guests, reid))
        count = cur.rowcount
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return count

    def Delete_Reserve(self, reid):
        # ** Method to delete an existing reserve in the database
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM reserve "
                 "WHERE reid = %s")
        cur.execute(query, (reid,))
        count = cur.rowcount
        if DatabaseOption() == 'd':
            self.db.docker_connection.commit()
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.heroku_connection.commit()
            self.dbh.close()
        cur.close()
        return count

    def Get_Total_Cost(self, rid, clid, startdate, enddate, season_markup):
        """
        Calculates the total cost of a hotel reservation with member discounts.
        Args:
            rid (int): Reservation ID.
            clid (int): Client ID.
            startdate (date): Start date of the reservation.
            enddate (date): End date of the reservation.
            season_markup (float): Seasonal price markup.
        Returns:
            float: The discounted total cost of the reservation.
        """
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT rprice, memberyear "
                 "FROM reserve "
                 "NATURAL INNER JOIN client "
                 "NATURAL INNER JOIN room "
                 "NATURAL INNER JOIN hotel "
                 "NATURAL INNER JOIN chains "
                 "WHERE rid = %s AND clid = %s ")
        # Validate and convert dates
        if type(startdate) == str or type(enddate) == str:
            startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
            enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
        cur.execute(query, (rid, clid))
        rprice, memberyear = cur.fetchone()
        num_days = (enddate - startdate).days
        # Calculate discount based on membership years
        member_discounts = {
            range(1, 5): 0.02,
            range(5, 10): 0.05,
            range(10, 15): 0.08,
            range(15, 1000): 0.12  # Assuming a sensible maximum
        }
        for years_range, discount_rate in member_discounts.items():
            if memberyear in years_range:
                member_discount = discount_rate
                break
        else:
            member_discount = 0
        total_cost = rprice * num_days * season_markup
        discount = total_cost * member_discount
        discounted_cost = round(total_cost - discount, 2)
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return discounted_cost

    """
    ------------------
    * TOOL OPERATIONS
    ------------------
    """

    def Get_Reserve_ByRoomUnavailable(self, ruid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT reid "
                 "FROM reserve "
                 "WHERE ruid = %s")
        cur.execute(query, (ruid,))
        reserve = cur.fetchone()
        if DatabaseOption() == 'd':
            self.db.close()
        elif DatabaseOption() == 'h':
            self.dbh.close()
        cur.close()
        return reserve

    def Get_RUID(self, reid):
        cur = 0
        if DatabaseOption() == 'd':
            cur = self.db.docker_connection.cursor()
        elif DatabaseOption() == 'h':
            cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT ruid "
                 "FROM reserve "
                 "WHERE reid = %s")
        cur.execute(query, (reid,))
        result = cur.fetchone()
        if type(result) == type(None):
            if DatabaseOption() == 'd':
                self.db.close()
            elif DatabaseOption() == 'h':
                self.dbh.close()
            cur.close()
            return None
        else:
            ruid = result[0]
            if DatabaseOption() == 'd':
                self.db.close()
            elif DatabaseOption() == 'h':
                self.dbh.close()
            cur.close()
            return ruid
