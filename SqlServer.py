import pyodbc


class SqlServer:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};" + f"SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};", autocommit=True)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        self.conn.close()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
