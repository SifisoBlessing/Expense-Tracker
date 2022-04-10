from API.DataBase import init_db
from API.Domain import DataHandler

class Controller:
    def setData(self,data):
        self.name = data[0].split("=")[1]
        self.surname =  data[1].split("=")[1]
        self.date =  data[2].split("=")[1]

    def postData(self):
        db = init_db.DBConnect()
        db.postData(self.name,self.surname,self.date)
        db.execute()

    def handleFile(self,filePath):
            dataHandler = DataHandler.HandleData(filePath)
            incomeAmount = dataHandler.getTotalIncomeAmount()
            expenseAmount = dataHandler.getTotalExpenseAmount()
            dateInYears = dataHandler.getDateInYears()
            yearlyIncome = dataHandler.getYearlyIncome()
            yearlyExpense = dataHandler.getYearlyExpense()

            return [incomeAmount, expenseAmount, dateInYears, yearlyIncome, yearlyExpense]