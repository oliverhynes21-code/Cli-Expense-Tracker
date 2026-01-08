#Expense tracker, uses csv file to store data

import csv, os
from datetime import date


def add_expense():
    expenseCategory = input(
        "Enter category (Housing/Transport/Food/Bills/Communication/Leisure/Healthcare/Clothing/Misc): ").strip().lower()

    if expenseCategory not in validCategories:
        print("Invalid category.")
    # Adding validation of categories as framework for future features (spending totals, potential GUI with tkinter, etc.)

    else:
        expenseItem = input("Enter item: ")

        # Validation coding for the price of the expense, repeatedly checks user input and asks for a numeric value until a satisfactory value is given
        priceAccepted = False
        while not priceAccepted:
            try:
                expensePrice = float(input("Enter price: "))
                priceAccepted = True
            except ValueError:
                print("Please enter a numeric value.")

        lastTotal = get_last_total("data/expenses.csv")
        newTotal = lastTotal + expensePrice

        # Opened file in context manager, doesn't need to be closed
        with open("data/expenses.csv", "a", newline='') as expenseFile:
            writer = csv.writer(expenseFile)

            if not fileExists:
                # Adding a header to the file if it is empty
                writer.writerow(["Date", "Category", "Item", "Price", "Cumulative Price"])

            writer.writerow([currentDate, expenseCategory, expenseItem, expensePrice, newTotal])

        update_category_totals()


def read_expenses():
    if not fileExists:
        print("No expenses found.")

    else:
        # Opened file in read mode
        with open("data/expenses.csv", "r") as expenseFile:
            reader = csv.reader(expenseFile)
            next(reader)
            print("Expenses:\n")
            for row in reader:
                # Removes the unnecessary characters from the row and adds a comma inbetween row elements
                # Also uses formatting rules to print an appealing table for the user
                print(f"{row[0]:<12} | {row[1]:<12} | {row[2]:<12} | £{float(row[3]):8.2f} | £{float(row[4]):8.2f}")


def get_last_total(filepath):
    try:
        with open(filepath, "r") as expenseFile:
            reader = csv.reader(expenseFile)
            # Skipping the header of the file to avoid value errors when converting price to a float
            next(reader)
            rows = list(reader)

            # Returns 0 if there are no previous totals
            if not rows:
                return 0.0

            return float(rows[-1][4])
    except FileNotFoundError:
        return 0.0


def write_category_totals(outputfile, totals):
    with open(outputfile, "w", newline='') as categoryTotalsFile:
        writer = csv.writer(categoryTotalsFile)

        if not categoryTotalsFileExists:
            writer.writerow(["Category", "Total"])

        else:
            # New concept for me, the items() function returns the key value pairs from the dictionary in tuples
            # The first part of the for loop is known as tuple unpacking, it assigns the two values from the key value pair
            # Which is now in a tuple to the two variables named, which are then used in the for loop to write to the CSV file
            for category, total in totals.items():
                writer.writerow([category, total])


def get_category_totals(sourcefile):
    totals = {}

    with open(sourcefile, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[1]
            price = float(row[3])

            totals[category] = totals.get(category, 0) + price

    return totals


def update_category_totals():
    totals = get_category_totals("data/expenses.csv")
    write_category_totals("data/categoryTotals.csv", totals)


def display_category_totals():
    try:
        with open("data/categoryTotals.csv", "r") as file:
            reader = csv.reader(file)
            print("Category Totals:\n")

            for row in reader:
                print(f"{row[0]:<12} £{float(row[1]):.2f}")
    except FileNotFoundError:
        print("No totals available yet.")


def calculate_monthly_totals():
    monthlyTotals = {}
    with open("data/expenses.csv", "r") as expenseFile:
        reader = csv.reader(expenseFile)
        next(reader)

        for row in reader:
            price = float(row[3])
            month = row[0][:7]
            category = row[1]

            if month not in monthlyTotals:
                monthlyTotals[month] = {}

            monthlyTotals[month][category] = monthlyTotals[month].get(month, 0) + price

    return monthlyTotals


def display_monthly_totals():
    monthlyTotals = calculate_monthly_totals()
    print("Monthly Totals:\n")

    for month, category in monthlyTotals.items():
        print(month)
        for category, total in category.items():
            print(f"    {category:<12} | £{total:.2f}")

userExit = False
validCategories = {"housing", "transport", "food", "bills", "communication", "leisure", "healthcare", "clothing",
                   "misc"}

while not userExit:

    currentDate = date.today().isoformat()
    fileExists = os.path.isfile("data/expenses.csv")
    categoryTotalsFileExists = os.path.isfile("data/categoryTotals.csv")

    print("\n-------- CLI Expense Tracker --------")
    userAction = int(input("1. Add Expense\n2. Read Expenses\n3. View Category Totals\n4. View Monthly Totals\n5. Quit\nSelect Action (1-5): "))

    if userAction == 1:
        add_expense()

    elif userAction == 2:
        read_expenses()

    elif userAction == 3:
        update_category_totals()
        display_category_totals()

    elif userAction == 4:
        display_monthly_totals()

    elif userAction == 5:
        confirm = ''
        while confirm not in ["y", "n"]:
            confirm = input("Are you sure you want to quit? (y/n): ").strip().lower()
            if confirm == "y":
                userExit = True
            elif confirm == "n":
                userExit = False
            else:
                print("Please respond with 'y' or 'n'.")