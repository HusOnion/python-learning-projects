from datetime import datetime
import csv

class expense:
    def __init__(self,name,amount,category,date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
    
    def __str__(self):
        return f"{self.name} | {self.amount} | {self.category} | {self.date.strftime('%d-%m-%Y')}"

expenses = []

def main():

    is_running = True
    while is_running:
        display(1)
        user = input_handling(1,5)
        
        if user == 1:
            if len(expenses) == 0:
                print("No expenses to show.")
            else:
                display(2)
        elif user == 2:
            add_expense()
        elif user == 3:
            show_summary()
        elif user == 4:
            export_to_csv()
        else:
            is_running = False
        



def display(num):
    # 1 to print the main display and 2 or any other number for the show expense display 
    if num == 1:
        print("1.Show expenses\n2.Add expense\n3.Summary\n4.Export data\n5.exit")
    else:
        for expense in expenses:
            print(expense)
        


def add_expense():
    while True:
        try:
            name = str(input("Enter the name: "))
            amount = float(input("Enter the amount: "))
            category = str(input("Enter the category: "))
            date_input = input("Enter the date (DD-MM-YYYY): ")
            date = datetime.strptime(date_input, "%d-%m-%Y").date()

            new_expense = expense(name,amount,category,date)
            expenses.append(new_expense)

            print("Expense Added Succesfuly.")
            break

        except ValueError:
            print("Value Error")


def show_summary():
    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0
    for expense in expenses:
        total += expense.amount

    print(f"Total spending: {total}")


def input_handling(n1,n2):
    while True:
        x = input(f"Enter your choice({n1},{n2}): ")
        try:
            x = int(x)
            if x > n2 or x < n1:
                print("Exceeded the range")
                continue
            break
        except ValueError:
            print("Value Error, Enter a number")
    
    return x

def export_to_csv():
    if not expenses:
        print("No expenses to export.")
        return

    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        # Header row
        writer.writerow(["Name", "Amount", "Category", "Date"])

        # Data rows
        for expense in expenses:
            writer.writerow([
                expense.name,
                expense.amount,
                expense.category,
                expense.date
            ])

    print("Data exported successfully to expenses.csv")

if __name__ == "__main__":
    main()
