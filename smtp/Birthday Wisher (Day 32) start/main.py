import smtplib
from datetime import datetime

# my_email = "polamanasa03@gmail.com"
# password = "uqbl xwsq yvri ztyf"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email, password  = password)
#     connection.sendmail(
#         from_addr = my_email,
#         to_addrs = "sulegaonpraveen@gmail.com", 
#         msg = "Subject:Test Email\n\n Hello dear"
#         )
# connection.close()

# present_date_time = datetime.now()
# print(present_date_time)
# present_date = datetime.date(present_date_time)
# print(present_date)
# present_time = datetime.time(present_date_time)
# print(present_time)
# print(present_date_time.year)
# print(present_date_time.day)
# present_weekday = present_date_time.weekday()
# print(present_weekday)

dob = datetime(year = 1996, month = 8, day = 21,hour=10, minute = 30, second = 30)
print(dob)




