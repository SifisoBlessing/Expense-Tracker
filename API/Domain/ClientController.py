import json
from API.DataBase import init_db
from API.Domain import DataHandler

class Controller:

    def __init__(self) -> None:
        self.db = init_db.DBConnect()

    def setData(self,data):
        self.name = data[0].split("=")[1]
        self.surname =  data[1].split("=")[1]
        self.date =  data[2].split("=")[1]

    def validateData(self):
        """
            return True if the user exists
        """
        value = self.db.getUserId(self.name,self.surname,self.date)
        if value.arraysize == 0:
            self.postData()
            self.db.execute()
            return False

        else:
            return True
        

    def postData(self):
        self.db.postData(self.name,self.surname,self.date)
        self.db.execute()

    def handleFile(self,filePath):
            dataHandler = DataHandler.HandleData(filePath)
            incomeAmount = dataHandler.getTotalIncomeAmount()
            expenseAmount = dataHandler.getTotalExpenseAmount()
            dateInYears = dataHandler.getDateInYears()
            yearlyIncome = dataHandler.getYearlyIncome()
            yearlyExpense = dataHandler.getYearlyExpense()

            data = [incomeAmount, expenseAmount, dateInYears, yearlyIncome, yearlyExpense]
            # self.db.saveFileData(data)

            return data

    def getFileData(self):
        id = self.db.getUserId(self.name,self.surname,self.date)
        data = self.db.getFileData(id)
        self.db.execute()

        return [data["summedIncome"],
            data["summedExpense"],
            json.loads(data["dateInYears"]),
            json.loads(data["yearlyIncome"]),
            json.loads(data["yearlyExpense"])
        ]