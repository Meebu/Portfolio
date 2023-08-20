import smtplib,ssl
import os

def send_email(message,email):
    host="smtp.gmail.com"
    port=465

    sender=email
    password=os.getenv("PASSWORD"   )

    reciever=email
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,reciever,message)