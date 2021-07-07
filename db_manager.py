import psycopg2


class DBManager():
    def __init__(self, user='postgres', password='pw', host='localhost', port=5432, database='instant'):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = self.connect()

    def connect(self):
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return conn

    def check_password(self, username, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT password FROM users WHERE username = '{username}';")
            for row in cursor:
                if row[0] == password:
                    return True
                return False

        except psycopg2.Error:
            self.connection = self.connect()
            return 'retry'

