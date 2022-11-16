# most popular way to handle API
import requests
import datetime
import smtplib
import time

def nearby(own_lat, own_lon):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # to handle errors automatically
    response.raise_for_status()
    # this gets actual data
    longitude = float(response.json()["iss_position"]["longitude"])
    latitude = float(response.json()["iss_position"]["latitude"])
    if own_lat-5 <= latitude <= own_lat+5 and own_lon-5<= longitude <= own_lon+5:
        return True
    else:
        return False

MY_LAT = 52.090736
MY_LON = 5.121420

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "formatted": 0
    }
    # this api requires you to put in longitude and latitude parameters
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour

    if sunset < time_now < sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if nearby() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="emailsenderday32@gmail.com", password="")
            connection.sendmail(from_addr="emailsenderday32@gmail.com", to_addrs="emailsenderday32@yahoo.com",
                                msg="Subject: Look UP\n\nISS is flying above you!")