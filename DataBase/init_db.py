import sqlite3
from datetime import datetime

class DBConnect:

    def __init__(self):
        self._connection = sqlite3.connect('resources/Database.db')
        with open('DataBase\schema.sql') as f:
            self._connection.executescript(f.read())

    def postData(self,name,surname,date):
        cur = self._connection.cursor()

        date = f"{date}".replace('-','/')
        print(date)

        cur.execute(f"""INSERT INTO clients( Fname, Lname, Bdate) 
        VALUES( {name}, {surname}, testing );""")

    def execute(self):
        self._connection.commit()
        self._connection.close()