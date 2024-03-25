import psycopg2


class Heroku_Database:

    def connect_heroku_db(self):
        heroku_db = {
            'host': 'ec2-54-152-144-84.compute-1.amazonaws.com',
            'database': 'd1brf8nquq7utk',
            'user': 'zvtlouizcmwqdp',
            'port': '5432',
            'password': '3a28954acdb4eac8b9870ea92ca4407d4d2d919bea1cd5deeb6f6e4af0e5b3b0'
        }
        return heroku_db

    def __init__(self):
        self.heroku_credentials = self.connect_heroku_db()
        self.heroku_connection = psycopg2.connect(
            host=self.heroku_credentials['host'],
            database=self.heroku_credentials['database'],
            user=self.heroku_credentials['user'],
            port=self.heroku_credentials['port'],
            password=self.heroku_credentials['password']
        )

    def close(self):
        self.heroku_connection.close()


class Docker_Database:

    def connect_docker_db(self):
        docker_db = {
            'host': 'localhost',
            'database': 'test1',
            'user': 'user1',
            'port': '5432',
            'password': 'user1'
        }
        return docker_db

    def __init__(self):
        self.docker_credentials = self.connect_docker_db()
        self.docker_connection = psycopg2.connect(
            host=self.docker_credentials['host'],
            database=self.docker_credentials['database'],
            user=self.docker_credentials['user'],
            port=self.docker_credentials['port'],
            password=self.docker_credentials['password']
        )

    def close(self):
        self.docker_connection.close()