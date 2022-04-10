import sqlite3

from urllib3 import Retry

class DBConnect:

    def __init__(self):
        self._connection = sqlite3.connect('API/resources/Database.db')
        with open('API/DataBase\schema.sql') as f:
            self._connection.executescript(f.read())


    def postData(self,name,surname,date):
        cur = self._connection.cursor()

        cur.execute(f"INSERT INTO clients( Fname, Lname, Bdate) VALUES( \"{name}\", \"{surname}\", \"{date}\" )")


    def saveFileData(self,data,id):
        cur = self._connection.cursor()

        summedIncome = data[0]
        summedExpense = data[1]
        dateInYears = data[2]
        yearlyIncome = data[3]
        yearlyExpense = data[4]

        cur.execute(f"""INSERT INTO ExpensesData(id, summedIncome, summedExpense, dateInYears, yearlyIncome, yearlyExpense ) 
        VALUES({id}, {summedIncome}, {summedExpense}, \"{dateInYears}\", \"{yearlyIncome}\", \"{yearlyExpense}\" )""")


    def getFileData(self,id):
        cur = self._connection.cursor()
        cur.row_factory = sqlite3.Row

        request = f"""SELECT * FROM  ExpensesData WHERE id=={id}"""
        cur.execute(request)
        data =  cur.fetchall()
        return data

    
    def getUserId(self,name,surname,date):
        cur = self._connection.cursor()
        cur.row_factory = sqlite3.Row

        request = f"""SELECT id FROM clients WHERE Fname== \"{name}\" AND Lname== \"{surname}\" AND Bdate== \"{date}\""""
        cur.execute(request)

        data =  cur.fetchall()
        return data

    def execute(self):
        self._connection.commit()
        self._connection.close()