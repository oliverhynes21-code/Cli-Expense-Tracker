# Cli-Expense-Tracker

## Overview
This project is a simple command-line tool which allows the user to track their expenses. It will include date, category, cost and this data will be written to a CSV database. The program will feature a CLI menu which allows the user to perform various functions, including the ability to add a new expense, read previously recorded expenses, view overall category totals, and view monthly category totals.

## Features
- Add new expenses
- Output current recorded expenses
- Output overall spending by category
- Output monthly spending by category
- Save to two external CSV files which can monitor all expenses and category totals

## Motivation for the project
I created this project as a way for myself to practice the fundamentals of python, including file handling by using context managers (with the with statement) and writing to CSV files. It also allowed me to gain a small amount of experience in structuring a small but functional program. I also tried to add more comments in my work where they were necessary, as this is a good habit to get into for future larger projects and potientially working in this field.

## What I learned
- How to write to CSV files
- How to use context managers as a more efficient way to handle files
- How to handle user input safely (validation)
- Tuple unpacking

## Future improvements
- Comparing total monthly cost with monthly income
- Ability to delete or modify previous records (though this may be out of my ability due to the limitations of CSV files and the difficulty of the workaround)
- Potentially in the far future, a GUI version with simple graphs (perhaps graphs totalling the user's spending on certain categories per month?)
