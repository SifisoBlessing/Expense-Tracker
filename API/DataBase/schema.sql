CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Fname TEXT NOT NULL, 
    Lname TEXT NOT NULL, 
    Bdate TEXT NOT NULL
    );

CREATE TABLE IF NOT EXISTS ExpensesData(
    id INTEGER PRIMARY KEY , 
    summedIncome INTEGER NOT NULL, 
    summedExpense INTEGER NOT NULL, 
    dateInYears TEXT NOT NULL,
    yearlyIncome TEXT NOT NULL,
    yearlyExpense TEXT NOT NULL
    );