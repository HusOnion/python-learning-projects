import smtplib, ssl
import os 



def send_email(message,emails_list):
    host = "smtp.gmail.com"
    port = 465

    username = "sawaftah.husam@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")
    for x in range(len(emails_list)):
        
        receiver = f"{emails_list[x]}"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host,port,context=context) as server:
            server.login(username,password)
            server.sendmail(username,receiver,message)


