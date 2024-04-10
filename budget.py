import csv
import os

# Function to load existing transactions from CSV file
def load_transactions(file_name):
    transactions = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                transactions.append(row)
    return transactions

# Function to save transactions to CSV file
def save_transactions(file_name, transactions):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Category", "Amount"])
        writer.writerows(transactions)

# Function to add a transaction
def add_transaction(transactions):
    transaction_type = input("Enter transaction type (Income/Expense): ").lower()
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    transactions.append([transaction_type, category, amount])

# Function to calculate budget
def calculate_budget(transactions):
    total_income = sum(float(row[2]) for row in transactions if row[0].lower() == 'income')
    total_expenses = sum(float(row[2]) for row in transactions if row[0].lower() == 'expense')
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to analyze expenses
def analyze_expenses(transactions):
    expenses_by_category = {}
    for row in transactions:
        if row[0].lower() == 'expense':
            category = row[1]
            amount = float(row[2])
            if category in expenses_by_category:
                expenses_by_category[category] += amount
            else:
                expenses_by_category[category] = amount
    return expenses_by_category

# Main function
def main():
    transactions_file = "transactions.csv"
    transactions = load_transactions(transactions_file)

    while True:
        print("\n===== Personal Budget Tracker =====")
        print("1. Add Transaction")
        print("2. Calculate Budget")
        print("3. Analyze Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction(transactions)
            save_transactions(transactions_file, transactions)
        elif choice == '2':
            remaining_budget = calculate_budget(transactions)
            print("Remaining Budget:", remaining_budget)
        elif choice == '3':
            expenses_by_category = analyze_expenses(transactions)
            print("Expenses by Category:")
            for category, amount in expenses_by_category.items():
                print(category + ":", amount)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
