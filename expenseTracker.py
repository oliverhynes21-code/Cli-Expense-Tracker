#Expense tracker, uses csv file to store data

import csv, os
from datetime import date

while True:

    currentDate = date.today().isoformat()
    fileExists = os.path.isfile("data/expenses.csv")

    print("-------- CLI Expense Tracker --------")
    userAction = int(input("1. Add Expense\n2. Read Expenses\n3. Quit\nSelect Action (1-3): "))

    if userAction == 1:
        expenseCategory = input("Enter expense category: ")
        expensePrice = float(input("Enter expense price: "))

        #Opened file in context manager, doesn't need to be closed
        with open("data/expenses.csv", "a", newline='') as expenseFile:
            writer = csv.writer(expenseFile)

            if not fileExists:
                #Adding a header to the file if it is empty
                writer.writerow(["Date", "Category", "Price"])

            writer.writerow([currentDate, expenseCategory, expensePrice])

    elif userAction == 2:
        if not fileExists:
            print("No expenses found.")
        else:
            #Opened file in read mode
            with open("data/expenses.csv", "r") as expenseFile:
                reader = csv.reader(expenseFile)
                for row in reader:
                    #Removes the unnecessary characters from the row and adds a comma inbetween row elements
                    print(*row, sep=",")

    elif userAction == 3:
        break
