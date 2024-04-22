import psycopg2


class Heroku_Database:

    def connect_heroku_db(self):
        heroku_db = {
            'host': 'ec2-44-194-65-158.compute-1.amazonaws.com',
            'database': 'd8e72jptcgd4rm',
            'user': 'hkvwkxakpcyzxr',
            'port': '5432',
            'password': '197ca7bdb19cc0b28a45ecff234ed8f5dce0d2cfb352aa28d6c8fdae06760250'
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
