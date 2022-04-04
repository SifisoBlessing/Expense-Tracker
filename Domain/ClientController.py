from DataBase import init_db

class Controller:
    def setData(self,data):
        self.name = data
        self.surname = data
        self.date = data

    def postData(self):
        db = init_db.DBConnect()
        db.postData(self.name,self.surname,self.date)
        db.execute()

    def getData(self):
        pass
