from datetime import datetime
import random
import smtplib

present_weekday = datetime.now().weekday()
print(present_weekday)
with open(file = "/Users/manasapola/PycharmProjects/Basicsofpython/smtp/Birthday Wisher (Day 32) start/quotes.txt", mode = 'r') as file:
        content=file.readlines()
        random_quote = random.choice(content)
        print(random_quote)

my_email = "polamanasa03@gmail.com"
password = "uqbl xwsq yvri ztyf"

if present_weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password  = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "pola.manasa@yahoo.com", 
            msg = f"Subject:Monday Motivational Quote\n\n {random_quote} "
            )
connection.close()