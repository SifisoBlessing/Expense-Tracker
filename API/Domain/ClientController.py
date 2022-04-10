import json
from API.DataBase import init_db
from API.Domain import DataHandler

class Controller:

    def __init__(self):
        self.db = init_db.DBConnect()

    def setData(self,data):
        self.name = data[0].split("=")[1]
        self.surname =  data[1].split("=")[1]
        self.date =  data[2].split("=")[1]

    def validateData(self):
        """
            return True if the user exists
        """
        db = init_db.DBConnect()

        value = db.getUserId(self.name,self.surname,self.date)
        if len(value) == 0:
            self.postData()
            db.execute()
            return False

        else:
            return True
        

    def postData(self):
        db = init_db.DBConnect()
        db.postData(self.name,self.surname,self.date)
        db.execute()

    def handleFile(self,filePath):
        db = init_db.DBConnect()

        dataHandler = DataHandler.HandleData(filePath)
        incomeAmount = dataHandler.getTotalIncomeAmount()
        expenseAmount = dataHandler.getTotalExpenseAmount()
        dateInYears = dataHandler.getDateInYears()
        yearlyIncome = dataHandler.getYearlyIncome()
        yearlyExpense = dataHandler.getYearlyExpense()

        data = [incomeAmount, expenseAmount, dateInYears, yearlyIncome, yearlyExpense]
        id = db.getUserId(self.name,self.surname,self.date)

        db.saveFileData(data,id[0]["id"])
        db.execute()

        return data

    def getFileData(self):
        db = init_db.DBConnect()
        id = db.getUserId(self.name,self.surname,self.date)
        data = db.getFileData(id[0]["id"])
        db.execute()
        return [data[0][1],
            data[0][2],
            json.loads(data[0][3]),
            json.loads(data[0][4]),
            json.loads(data[0][5])
        ]