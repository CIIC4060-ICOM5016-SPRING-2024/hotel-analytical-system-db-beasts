# ** Importing Docker_Database from db module
from db import Docker_Database, Heroku_Database


# ** Class for handling database operations related to employee model
class Employee_Model_Dao:
    def __init__(self):
        # ** Initializing database connection to Docker_Database
        # self.db = Docker_Database()
        self.dbh = Heroku_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to fetch all employees from the database
    def Get_All_Employees(self):
        # cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM employee "
                 "order by eid")
        cur.execute(query)
        employees_list = cur.fetchall()
        # self.db.close()
        self.dbh.close()
        cur.close()
        return employees_list

    # ** Method to fetch a specific employee by its ID from the database
    def Get_Employee(self, eid):
        # cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = ("SELECT * "
                 "FROM employee "
                 "WHERE eid = %s")
        cur.execute(query, (eid,))
        employee = cur.fetchone()
        # self.db.close()
        self.dbh.close()
        cur.close()
        return employee

    # ** Method to add a new employee to the database

    def Post_Employee(self, hid, fname, lname, age, position, salary):
        # cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = ("INSERT INTO employee (hid, fname, lname, age, position, salary)"
                 "VALUES (%s, %s, %s, %s, %s, %s)"
                 "returning eid")
        cur.execute(query, (hid, fname, lname, age, position, salary))
        result = cur.fetchone()[0]
        # self.db.docker_connection.commit()
        self.dbh.heroku_connection.commit()
        # self.db.close()
        self.dbh.close()
        cur.close()
        return result

    # ** Method to update an existing employee in the database
    def Put_Employee(self, eid, hid, fname, lname, age, position, salary):
        # cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = ("UPDATE employee "
                 "SET hid = %s, fname = %s, lname = %s, age = %s, position = %s, salary = %s "
                 "WHERE eid = %s")
        cur.execute(query, (hid, fname, lname, age, position, salary, eid))
        count = cur.rowcount
        # self.db.docker_connection.commit()
        self.dbh.heroku_connection.commit()
        # self.db.close()
        self.dbh.close()
        cur.close()
        return count

        # ** Method to delete an existing employee in the database (WIP, Docker is down)

    def Delete_Employee(self, eid):
        # cur = self.db.docker_connection.cursor()
        cur = self.dbh.heroku_connection.cursor()
        query = ("DELETE FROM employee "
                 "WHERE eid = %s")
        try:
            cur.execute(query, (eid,))
            count = cur.rowcount
            # self.db.docker_connection.commit()
            self.dbh.heroku_connection.commit()
            # self.db.close()
            self.dbh.close()
            cur.close()
            return count
        except:
            # self.db.close()
            self.dbh.close()
            cur.close()
            return "Error deleting the employee"
