#TASK2: PERSONAL BUDGET TRACKER

import os
# File to store transactions
FILE_NAME = 'transactions.txt'

# Load transactions from file if it exists
def load_transactions():
    transactions = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                type_, category, amount = line.strip().split(',')
                transactions.append({
                    'type': type_,
                    'category': category,
                    'amount': float(amount)
                })
    return transactions

# Save transactions to file
def save_transactions(transactions):
    with open(FILE_NAME, 'w') as file:
        for transaction in transactions:
            line = f"{transaction['type']},{transaction['category']},{transaction['amount']}\n"
            file.write(line)

# Load existing transactions
transactions = load_transactions()

def add_transaction(type_, category, amount):
    transaction = {
        'type': type_,
        'category': category,
        'amount': amount
    }
    transactions.append(transaction)

def calculate_budget():
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    return total_income - total_expenses

def expense_analysis():
    category_totals = {}
    for t in transactions:
        if t['type'] == 'expense':
            if t['category'] not in category_totals:
                category_totals[t['category']] = 0
            category_totals[t['category']] += t['amount']
    return category_totals

def main():
    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget")
        print("4. Expense Analysis")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            add_transaction('income', category, amount)
            save_transactions(transactions)

        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            add_transaction('expense', category, amount)
            save_transactions(transactions)

        elif choice == '3':
            budget = calculate_budget()
            print(f"Remaining budget: ₹{budget:.2f}")

        elif choice == '4':
            analysis = expense_analysis()
            print("Expense Analysis by Category:")
            for category, total in analysis.items():
                print(f"{category}: ₹{total:.2f}")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
