import sqlite3

class DBConnect:

    def __init__(self):
        self._connection = sqlite3.connect('API/resources/Database.db')
        with open('API/DataBase\schema.sql') as f:
            self._connection.executescript(f.read())


    def postData(self,name,surname,date):
        cur = self._connection.cursor()

        cur.execute(f"INSERT INTO clients( Fname, Lname, Bdate) VALUES( \"{name}\", \"{surname}\", \"{date}\" )")


    def saveFileData(self,data):
        cur = self._connection.cursor()

        summedIncome = data[0]
        summedExpense = data[1]
        dateInYears = data[2]
        yearlyIncome = data[3]
        yearlyExpense = data[4]

        cur.execute(f"""INSERT INTO ExpensesData( summedIncome, summedExpense, dateInYears, yearlyIncome,yearlyExpense ) 
        VALUES( {summedIncome}, {summedExpense}, \"{dateInYears}\", \"{yearlyIncome}\", \"{yearlyExpense}\" )""")


    def getFileData(self,id):
        cur = self._connection.cursor()
        cur.row_factory = sqlite3.Row

        request = f"""SELECT FROM * ExpensesData WHERE id=={id}"""
        cur.execute(request)

        return cur.execute(request)

    
    def getUserId(self,name,surname,date):
        cur = self._connection.cursor()
        cur.row_factory = sqlite3.Row

        request = f"""SELECT FROM id ExpensesData WHERE Fname=={name}, Lname=={surname}, Bdate=={date}"""
        cur.execute(request)

        return cur.fetchall()


    def execute(self):
        self._connection.commit()
        self._connection.close()