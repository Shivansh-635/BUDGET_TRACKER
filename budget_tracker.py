budget = 0
expenses = []
def set_budget():
    global budget
    while True:
        try:
            amount=int(input("Enter your monthly budget (in Rs):"))
            if amount < 0:
                print("Budget cannot be negative. Try again.")
                continue
            budget = amount
            print("Budget set successfully!")
            break
        except ValueError:
            print("Please enter a valid number for your budget.")
def add_expense():
    global expenses
    item = input("Expense name: ").strip()
    if not item:
        print("Expense name cannot be empty.")
        return
    while True:
        try:
            amount=int(input("Amount spent (in Rs): "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            expenses.append({"item": item, "amount": amount})
            print("Expense added.")
            break
        except ValueError:
            print("Please enter a valid number for amount.")
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("Expense List:")
    for i,e in enumerate(expenses, 1):
        print(f"{i}.{e['item']}-Rs{e['amount']}")
def remaining_budget():
    total_spent=sum(e["amount"] for e in expenses)
    remaining=budget-total_spent
    print(f"Total Budget: Rs{budget}")
    print(f"Total Spent: Rs{total_spent}")
    print(f"Remaining Balance: Rs{remaining}")
while True:
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Remaining Budget")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        set_budget()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_expenses()
    elif choice == "4":
        remaining_budget()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")
