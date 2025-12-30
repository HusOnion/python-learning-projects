def main():

    balance = 0

    is_running = True 

    while is_running:
        print("*****************************")
        print("           STC BANK          ")
        print("*****************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("***************************************")

        user = input("Choose a number (1-4): ")

        if not user.isdigit() or len(user) > 1 or int(user) > 4 or int(user) < 0:
            print("Enter a valid input,Please")
            continue

        user = int(user)


        if user == 1:
            show_balance(balance)
        
        elif user == 2:
            balance += deposit()

        elif user == 3:
            balance -= withdraw(balance)

        elif user == 4:
            print("Thanks for using STC Bank!")
            is_running = False



def show_balance(balance):
    print(f"Your balance is: ${balance}")

def deposit():
    amount = input("Enter the amount you want to deposit: $")

    if not amount.isdigit() or int(amount) < 0:
        print("Enter a valid input,Please")
    
    else:
        return int(amount)
        

def withdraw(balance):
    amount = input("Enter the amount you want to withdraw: $")
    
    if not amount.isdigit() or int(amount) < 0:
        print("Enter a valid input,Please")
    elif int(amount) > balance:
        print("Sorry, Not Enough Funds")
    
    else:
        return int(amount)


if __name__ == "__main__":
    main()
