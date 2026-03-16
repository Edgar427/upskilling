from expense import Expense
import calendar
import datetime


def main():

    expense_file_path = "expenses.csv"
    budget = 2000

    print(f"Running expense tracker")
    #expense = get_user_expense()
    #print(expense)

    #save_expense(expense, expense_file_path)

    summarize_expense(budget, expense_file_path)


def get_user_expense():
    print(f"Getting user expense")
    expense_name = input(f"Enter expense name: ")
    expense_amount = float(input(f"Enter expense amount: "))
    
    expense_category = ["Food", "Work", "Fun", "Home", "Misc"]
    
    while True:
        print(f"Choose a category")
        for i, category_name in enumerate(expense_category):
            print(f"{i + 1} . {category_name}")
        
        value_range = f"[1 - {len(expense_category)}]"

        selected_index = int(input(f"Choose a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            print(f"{selected_category}")

            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount)
            return new_expense
        else:

            print(f"Invalid category please choose again")
        
        
def save_expense(expense:Expense, expense_file_path):

    print(f"saving user expense {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(budget,expense_file_path):
    print(f"summarizing user expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:

        lines = f.readlines()
        for line in lines:
            #stripped_line = line.strip()
            expense_name, expense_amount, expense_category = line.strip().split(",")
            
            line_expense = Expense(name = expense_name, amount = float(expense_amount) , category = expense_category )
            #print(line_expense)
            expenses.append(line_expense)
            print(line_expense)
    
    
        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
   
    print(f"Expenses by category")
    for key, amount in amount_by_category.items():
        print(f"{key}. ${amount}")


    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent {total_spent:.2f} in total")
     
    remaining_budget = budget - total_spent
    print(f"You have {remaining_budget:.2f} left in your bank")
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"Budget per day = {daily_budget}"))

   
def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
