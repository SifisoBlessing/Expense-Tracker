import pandas as pd

class HandleData:
    _dateInMonths = []
    _monthlyIncome = []
    _monthlyExpense = []
    
    def __init__(self,filePath):
        self._df_sheet_index = pd.read_excel(filePath, sheet_name=0)
        self._incomes = [x for x in self._df_sheet_index["income amount"]]
        self._expenses = [x for x in self._df_sheet_index["expense amount"]]
        self.dates = self._df_sheet_index["date"]

    def getTotalExpenseAmount(self):
        amount = 0
        for val in self._expenses:
            amount += int(val)
        return amount

    def getTotalIncomeAmount(self):
        amount = 0
        for val in self._incomes:
            amount += int(val)
        return amount

    def getDateInYears(self):
        dates = [f"{x}".replace('-','/') for x in self.dates]
        years = [f"{x}".split('/')[2] for x in dates]
        incomeAmount = 0
        expenseAmount = 0

        self._dateInMonths.append(int(years[0]))
        for i in range(len(years)):
            incomeAmount += self._incomes[i]
            expenseAmount += self._expenses[i]

            if i == len(years)-1:
                self._monthlyIncome.append(incomeAmount)
                self._monthlyExpense.append(expenseAmount)

            if int(years[0]) > self._dateInMonths[-1]:
                self._dateInMonths.append(int(years[0]))
                self._monthlyIncome.append(incomeAmount)
                self._monthlyExpense.append(expenseAmount)
                incomeAmount = 0
                expenseAmount = 0
        return self._dateInMonths

    def getYearlyIncome(self):
        return self._monthlyIncome

    def getYearlyExpense(self):
        return self._monthlyExpense
    