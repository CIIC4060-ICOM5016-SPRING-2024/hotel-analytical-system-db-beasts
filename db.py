import psycopg2


class Heroku_Database:

    def connect_heroku_db(self):
        heroku_db = {
            'host': 'ec2-35-170-27-172.compute-1.amazonaws.com',
            'database': 'd233pmhuh6h64h',
            'user': 'izafoudsvarjpv',
            'port': '5432',
            'password': '02f14a70c06a81b2d5c2bc94a2f4aa05849295ec5317f624d97f10e3b077cbc2'
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
