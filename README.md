# Expense-Tracker
A simple web application that gets an excel sheet from a client and displays the data in graphs.

## Requirements:
1. Python
2. Flask

## Application setup steps:
1. pip install flask
2. pip install pandas
3. python app.py
4. url = http://localhost:8080

## File format expected
1. File should be an excel file
2. ensure that the data is stored in sheet=0
3. Data example:
|A          |    B       |    C   |
|-----------|----------|----------|
|date       |  expense |  income  |
|22/01/2022 |   500    |   200    |
|25/01/2022 |   50     |   201    |


## Architecture:
The project follows a simple Domain Layered Architecture