import sqlite3

class DBConnect:

    def __init__(self):
        _connection = sqlite3.connect('Database.db')
        with open('schema.sql') as f:
            _connection.executescript(f.read())

    def postData(self,name,surname,date):
        cur = self._connection.cursor()

        cur.execute(f"INSERT INTO clients (name, surname, date) VALUES ({name}, {surname}, {date})")

    def execute(self):
        self._connection.commit()
        self._connection.close()