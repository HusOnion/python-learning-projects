from searchArticles import search_for_articles
from generateArticle import generate_article
from user_display import get_emails,get_query,get_time_range
from send_email import send_email
import os


query = get_query()
time_range = get_time_range()

search_results = search_for_articles(query,time_range)

response = generate_article(search_results,query)

while True:
    try:
        x = input("Do you want to send it to email or save it in your pc? (1.for email, 2.for pc): ")
        x = int(x)
        if x == 1:
            body = "Subject: The Article\n\n" + response + " \n\n Thats it for today"
            body = body.encode("utf-8")
            emails_list = get_emails()
            send_email(body, emails_list)
            break
        elif x == 2:
            file_name = input("Enter the file name: ")
            path = f"C:\\Users\\hussa\\Desktop\\{file_name}.txt"
            with open(path, 'w') as file:
                file.write(response)
            break
        else:
            print("Exceeded the values!")
            continue
    except ValueError:
        print("Enter a vaild input!")


print("DONE")
