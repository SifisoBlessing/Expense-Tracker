import os
from DataBase import init_db
import pandas as pd

class Controller:
    def setData(self,data):
        self.name = data
        self.surname = data
        self.date = data

    def postData(self):
        db = init_db.DBConnect()
        db.postData(self.name,self.surname,self.date)
        db.execute()

    def handleFile(self,filePath):
        df_sheet_index = pd.read_excel(filePath, sheet_name=1)
        print(df_sheet_index)