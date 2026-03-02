
def category():
    categories = ["business","entertainment"
                  ,"general","health",
                  "science","sports","technology"]
    print("Which category do you want?")
    print("1. business")
    print("2. entertainment")
    print("3. general")
    print("4. health")
    print("5. science")
    print("6. sports")
    print("7. technology")

    user_category = input_handling(1,7)
    return categories[user_category-1]



def content():
    print("Do you want?")
    print("1. Full articles")
    print("2. Short summary")

    #this will return 1 or 2 to use it in the main :) 
    return input_handling(1,2)



def get_emails():
    while True:
        user_input = input("Enter emails to send to (comma separated): ")

        email_list = [email.strip() for email in user_input.split(",")]

        invalid_emails = [email for email in email_list if "@gmail.com" not in email]

        if invalid_emails:
            print(f"Invalid emails detected: {invalid_emails}")
            print("Please enter only valid Gmail addresses.\n")
            continue

        return email_list




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
            print("Value Error, Enter a number!")
    
    return x
    
