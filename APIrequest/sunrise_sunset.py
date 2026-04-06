import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 33.372972
MY_LNG = -86.847609
email = "polamanasa03@gmail.com"
password = "uqbl xwsq yvri ztyf"
reciever_email = "pola.manasa@yahoo.com"

def is_iss_overhead():
    iss_response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if ((MY_LAT <= iss_latitude + 5 or MY_LAT >= iss_latitude - 5) and (MY_LNG <= iss_longitude + 5 or MY_LNG >= iss_longitude - 5)):
        return True

def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0,
    }
    response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters, timeout=5)
    response.raise_for_status()
    data = response.json()
    sunrise_date = data["results"]["sunrise"].split("T")
    sunset_date = data["results"]["sunset"].split("T")
    sunrise_hour = int(sunrise_date[1].split(":")[0])
    sunset_hour = int(sunset_date[1].split(":")[0])
    time_now = datetime.now()
    hour_time_now = time_now.hour
    if(time_now.hour >= sunset_hour or time_now.hour <= sunrise_hour):
        return True



while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = email, password  = password)
            connection.sendmail(
                from_addr = email,
                to_addrs = reciever_email, 
                msg = f"Subject:ISS notifier\n\n Please look up, the iss is overhead of you"
                )
        connection.close()