import requests
from datetime import datetime
import smtplib
import time

# 40.714086,285.996180
MY_LAT = 40.714086
MY_LONG = 285.996180
RANGE = 5

MY_ACCOUNT = "auteforpt@yahoo.com"
PASSWORD = "ngzxqsctibcbbjou"
LOCAL_SOLAR_OFFSET = 5

def utc_to_lst(utc):
    """convert UTC into local solar time, by subtract or add  with time zone"""
    # in NY, the local solar offset = 5, USA is substract Time zone from UTC
    if utc - LOCAL_SOLAR_OFFSET > 0:
        return utc - LOCAL_SOLAR_OFFSET
    elif utc - LOCAL_SOLAR_OFFSET < 0:
        return 24 + (utc - LOCAL_SOLAR_OFFSET)
    else:
        return 0

def is_iss_over_head():
    # TODO : use ISS API to get iss location
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    longitude = float(data_iss["iss_position"]["longitude"])
    latitude = float(data_iss["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    # print(iss_position)

    if MY_LONG - RANGE <= iss_position[0] <= MY_LONG + RANGE and MY_LAT - RANGE <= iss_position[1] <= MY_LAT + RANGE:
        return True


# TODO : use sunrise sunset API to get time of sunrise and sunset in specific location
def is_dark():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response_sunrise_sunset = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response_sunrise_sunset.raise_for_status()
    data_sunrise_sunset = response_sunrise_sunset.json()
    print(f"UTC:{data_sunrise_sunset}")
    sunrise = int(data_sunrise_sunset["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sunrise_sunset["results"]["sunset"].split("T")[1].split(":")[0])
    # print(f"sunrise:{sunrise}")
    # print(f"sunset: {sunset}")
    # print(f"sunrise in local solar is :{utc_to_lst(sunrise)}")
    # print(f"sunset in local solar is :{utc_to_lst(sunset)}")


    # TODO: get current time
    now = datetime.now()
    print(f"Now hour is {now.hour}")
    if now.hour not in range(utc_to_lst(sunrise), utc_to_lst(sunset)):
        print("it's dark right now")
        return True

    # TODO: detect location, if it is in range then send email


iss_position = (285.996180 - 4, 40.714086)
# while True:
#     time.sleep(60)
if is_dark() and is_iss_over_head():
    print("I'am here")
    # with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_ACCOUNT, password=PASSWORD)
    #     connection.sendmail(from_addr=MY_ACCOUNT,
    #                         to_addrs=MY_ACCOUNT,
    #                         msg="Subject: Look up\n\n ISS is over your head.")
else:
    print("position: Not Yet")
