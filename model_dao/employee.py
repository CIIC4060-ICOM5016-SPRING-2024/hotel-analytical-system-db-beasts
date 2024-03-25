# Importing Docker_Database from db module
from db import Docker_Database


# Class for handling database operations related to employee model
class Employee_Model_Dao:
    def __init__(self):
        # Initializing database connection to Docker_Database
        self.db = Docker_Database()

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    def Get_All_Employees(self):
        cur = self.db.docker_connection.cursor()
        query = "SELECT * FROM employee order by eid"
        cur.execute(query)
        employees_list = cur.fetchall()
        self.db.close()
        cur.close()
        return employees_list
