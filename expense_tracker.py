from dateutil.utils import today

from expense import Expense

from datetime import date

budget = 0

def main():
    print ("Running Expense Tracker!")
    expense_file_path = "expenses.csv"
   
    expense = None
    while True:
        print("Welcome to the Expense Tracker!")
        print("Please choose an option:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        if user_choice == 1:
            expense = get_user_expense()
            print(f"you have entered {expense}")
        elif user_choice == 2:
            read_expenses_from_file(expense_file_path)
        elif user_choice == 3:
            track_budget(expense_file_path)
        elif user_choice == 4:
            save_expense_to_file(expense,expense_file_path)
        elif user_choice == 5:
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")


            


def get_user_expense():
    try:
        expense_name = input("Enter expense name: ")        
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return None
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
                
                new_expense = Expense(desc=expense_name, category=selected_category, amount=amount, date=date.today())
                return new_expense
            else:
                print("Invalid category. Please try again!")

def save_expense_to_file(expense, file_path):
    try:
        with open(file_path, "a") as file:
            file.write(f"{{'date': '{expense.date}', 'category': '{expense.category}', 'amount':{expense.amount}, 'description':'{expense.desc}' }}" + "\n")
        print(f"Expense saved to {file_path} successfully!")
    except Exception as e:
         print(f"Error saving expenses to {file_path}.")

def read_expenses_from_file(file_path):
    try:
        list_of_expenses = []    
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                expense_dict = eval(line)
                expense = Expense(
                    desc=expense_dict['description'],
                    category=expense_dict['category'],
                    amount=expense_dict['amount'],
                    date=expense_dict['date']
                )
            
                list_of_expenses.append(expense)
    except (IOError, json.JSONDecodeError):
        print(f"Error reading expenses from {file_path}.")            

    print("Expenses read from file: ")
    for expense in list_of_expenses:
        print(expense)

 

def track_budget( file_path):
    global budget
    if budget == 0:
        try:
            budget = float(input("Enter your budget: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            return

    total_expenses = 0
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                expense_dict = eval(line)            
                total_expenses += float(expense_dict['amount'])
    except (IOError, json.JSONDecodeError):
        print(f"Error reading expenses from {file_path}.")
        return
    
    if total_expenses > budget:
        print("You have exceeded your budget!\n\n")
    else:
        print(f"You have {budget-total_expenses}  left in your budget! \n\n")



if __name__ == '__main__':
    main()