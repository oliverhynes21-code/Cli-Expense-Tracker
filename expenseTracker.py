#Expense tracker, uses csv file to store data

import csv, os
from datetime import date

userExit = False
validCategories = {"housing", "transport", "food", "bills", "communication", "leisure", "healthcare", "clothing", "misc"}

while not userExit:

    currentDate = date.today().isoformat()
    fileExists = os.path.isfile("data/expenses.csv")

    print("-------- CLI Expense Tracker --------")
    userAction = int(input("1. Add Expense\n2. Read Expenses\n3. Quit\nSelect Action (1-3): "))

    if userAction == 1:
        expenseCategory = input("Enter category (Housing/Transport/Food/Bills/Communication/Leisure/Healthcare/Clothing/Misc): ").strip().lower()

        if expenseCategory not in validCategories:
            print("Invalid category.")
        #Adding validation of categories as framework for future features (spending totals, potential GUI with tkinter, etc.)

        else:
            expenseItem = input("Enter item: ")

            #Validation coding for the price of the expense, repeatedly checks user input and asks for a numeric value until a satisfactory value is given
            priceAccepted = False
            while not priceAccepted:
                try:
                    expensePrice = float(input("Enter price: "))
                    priceAccepted = True
                except ValueError:
                    print("Please enter a numeric value.")

            #Opened file in context manager, doesn't need to be closed
            with open("data/expenses.csv", "a", newline='') as expenseFile:
                writer = csv.writer(expenseFile)

                if not fileExists:
                    #Adding a header to the file if it is empty
                    writer.writerow(["Date", "Category", "Item", "Price"])

                writer.writerow([currentDate, expenseCategory,expenseItem, expensePrice])

    elif userAction == 2:
        if not fileExists:
            print("No expenses found.")

        else:
            #Opened file in read mode
            with open("data/expenses.csv", "r") as expenseFile:
                reader = csv.reader(expenseFile)
                for row in reader:
                    #Removes the unnecessary characters from the row and adds a comma inbetween row elements
                    print(f"{row[0]} | {row[1]} | {row[2]} | £{row[3]}")

    elif userAction == 3:
        userExit = True
