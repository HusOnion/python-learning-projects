
def get_time_range():
    time_range = ["day","week"
                  ,"month","year"]
    print("Which category do you want?")
    print("1. Day")
    print("2. Week")
    print("3. month")
    print("4. Year")

    user_category = input_handling(1,4)
    return time_range[user_category-1]



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
    

def get_query():
    while True:
        try:
            query = input("Enter the topic that you want to serach about\n"+
                            "Ex.AI in modern life :")
            str(query)
            return query

        except ValueError:
            print("please enter a vaild input!")

        


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
    