from expense import Expense
import calendar
import datetime


def main():
    print ("Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000
    expense = get_user_expense()
    print(expense)
    save_expense_to_file(expense, expense_file_path)

    read_expenses_from_file(expense_file_path)

def get_user_expense():
    expense_name = input("Enter expense name: ")
    print("You entered: " + expense_name)
    amount = input("Enter expense amount: ")
    print("You entered: " + amount)
    expense_categories = [
        "Food",
        "utilities",
        "Work",
        "Fun",
        "Misc",
    ]
    while True:
        print("Enter expense category: ")
        
        for i, category_name in enumerate(expense_categories):
            
            selected_index = int(input("1 Food, 2 Home, 3 Work, 4 Fun, 5 Misc: ")) -1
            print(f"{selected_index+1} You entered: " + category_name)
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                print("you choose category: " + selected_category)
                
                new_expense = Expense(
                     name=expense_name, category=selected_category, amount=amount
                 )
                return new_expense
            else:
                print("Invalid category. Please try again!")

def save_expense_to_file(expense, file_path):
    with open(file_path, "a") as file:
         file.write(f"{expense.name},{expense.amount},{expense.category}\n")
    print(f"Expense saved to {file_path} successfully!")

def read_expenses_from_file(file_path):

    list_of_expenses = []
    total_expenses = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, amount, category = line.strip().split(",")
            expense = Expense(name=name, amount=amount, category=category)
            total_expenses += int(expense.amount)
            list_of_expenses.append(expense)

    print("Expenses read from file: ")
    for expense in list_of_expenses:
        print(expense)

    print(f"Total expenses: ${total_expenses:.2f}")



if __name__ == '__main__':
    main()