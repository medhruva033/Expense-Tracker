import json
import os
from datetime import datetime

FILENAME = "expenses.json"

CATEGORIES = ["Food", "Transportation", "Entertainment", "Utilities", "Miscellaneous"]


if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as file:
        json.dump([], file)

def read_expenses():
    with open(FILENAME, 'r') as file:
        return json.load(file)


def write_expenses(expenses):
    with open(FILENAME, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    print("Add a new expense:")
    try:
        amount = float(input("Enter expense amount: "))
        print("Categories:", ", ".join(CATEGORIES))
        category = input(f"Choose a category ({', '.join(CATEGORIES)}): ").capitalize()
        if category not in CATEGORIES:
            print(f"Invalid category. Defaulting to 'Miscellaneous'.")
            category = "Miscellaneous"
        description = input("Enter description (optional): ")
        date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
        
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
        else:
            
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Using today's date.")
                date = datetime.today().strftime('%Y-%m-%d')

        
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        expenses = read_expenses()
        expenses.append(expense)
        write_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter the correct data.")

def analyze_expenses():
    expenses = read_expenses()

    monthly_expenses = {}
    category_expenses = {category: 0 for category in CATEGORIES}
    
    for expense in expenses:
        month = expense["date"][:7]  # YYYY-MM
        monthly_expenses.setdefault(month, 0)
        monthly_expenses[month] += expense["amount"]
        
        category_expenses[expense["category"]] += expense["amount"]

    print("\nMonthly Summary:")
    for month, total in monthly_expenses.items():
        print(f"{month}: ${total:.2f}")

    print("\nCategory-wise Expenditure:")
    for category, total in category_expenses.items():
        print(f"{category}: ${total:.2f}")

def view_expenses():
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['date']} - ${expense['amount']} - {expense['category']} - {expense['description']}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Analyze expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_expenses()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()

