from API.DataBase import init_db
import pandas as pd

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
        try:
            df_sheet_index = pd.read_excel(filePath, sheet_name=0)
            expense_amount = 0
            income_amount = 0

            dates = [f"{x}".replace('-','/') for x in df_sheet_index["date"]]
            incomes = [x for x in df_sheet_index["income amount"]]
            expenses = [x for x in df_sheet_index["expense amount"]]

            for val in df_sheet_index["expense amount"]:
                expense_amount += int(val)

            
            for val in df_sheet_index["income amount"]:
                income_amount += int(val)
        except:
            raise Exception

        return [income_amount,expense_amount,dates,incomes,expenses]