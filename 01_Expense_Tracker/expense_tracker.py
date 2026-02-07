expense_list = []


def add_expense():
    expense_amount = float(input("Enter expense amount: "))
    expense_catagory = input("Enter expense category: ")
    expense_note = input("Enter expense note: ")
    expense = {"Amount": expense_amount, "Category": expense_catagory, "Note": expense_note}

    expense_list.append(expense)
    print("Expense added Successfully", expense)

def view_expenses():
    if not expense_list:
        print("No expenses to show.") 
        return
    total = 0
    for expense in expense_list:
        total += expense["Amount"]
    print("Total Expenses = " , total)

def category_summary():
    if not expense_list:
        print("No expenses to show.")
        return
    catagory_totals = {}
    for expense in expense_list:
        category = expense["Category"]
        amount = expense["Amount"]
        if category in catagory_totals:
            catagory_totals[category] += amount
        else:
            catagory_totals[category] = amount

    for category, total in catagory_totals.items():
        print(f"Category: {category}, Total: {total}")

def save_to_file(filename="expenses.txt"):
    with open(filename, 'w') as file:
        for expense in expense_list:
            file.write(f"{expense['Amount']},{expense['Category']},{expense['Note']}\n")


def menu():
    while True:
        print("-------Expense Tracker Menu------")
        print("1.Add expense")
        print("2.View Expenses")
        print("3.Catagory wise Summary")
        print("4.Save data to file")
        print("5.exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Add expenses selected")
            add_expense()
        elif choice =='2':
            print("View expenses selected")
            view_expenses()
        elif choice == '3':
            print("Catagory wise Summary selected")
            category_summary()
        elif choice == '4':
            print("Save data to file selected")
            save_to_file()
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")
menu()


