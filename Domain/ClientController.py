import os
from DataBase import init_db
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
        df_sheet_index = pd.read_excel(filePath, sheet_name=0)
        print(df_sheet_index)