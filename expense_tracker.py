expenses = []

def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Amount Spent")
    print("4. Save & Exit")

def add_expense():
    name = input("\nEnter expense name: ")
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, Shopping, Other): ")

    expenses.append({"name": name, "amount": float(amount), "category": category})
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    print("\n--- Your Expenses ---")
    print("{:<5} {:<15} {:<10} {:<10}".format("No.", "Name", "Amount", "Category"))

    for i, expense in enumerate(expenses, start=1):
        print("{:<5} {:<15} {:<10} {:<10}".format(i, expense["name"], expense["amount"], expense["category"]))

def total_spent():
    total = sum(exp["amount"] for exp in expenses)
    print("\nTotal money spent:", total)

def save_to_file():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['name']}, {expense['amount']}, {expense['category']}\n")
    print("\nExpenses saved to expenses.txt")

while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        save_to_file()
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice, please try again.")

