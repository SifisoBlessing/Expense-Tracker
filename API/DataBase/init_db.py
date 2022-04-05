import sqlite3

class DBConnect:

    def __init__(self):
        self._connection = sqlite3.connect('API/resources/Database.db')
        with open('API/DataBase\schema.sql') as f:
            self._connection.executescript(f.read())

    def postData(self,name,surname,date):
        cur = self._connection.cursor()

        cur.execute(f"INSERT INTO clients( Fname, Lname, Bdate) VALUES( \"{name}\", \"{surname}\", \"{date}\" )")

    def execute(self):
        self._connection.commit()
        self._connection.close()