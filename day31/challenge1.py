import datetime as dt
import random
import smtplib

# --------------send motivation quote from file to mailbox at specific weekday----------------------#

# Yahoo! SMTP server address: smtp.mail.yahoo.com

def send_mail(msg):
    my_email = "auteforpt@yahoo.com"
    password = "uunaoprbuwckqzyx"

    with smtplib.SMTP("smtp.mail.yahoo.com") as connnetion:
        connnetion.starttls()
        connnetion.login(user=my_email, password=password)
        connnetion.sendmail(from_addr=my_email,
                            to_addrs="lna483018@gmail.com",
                            msg=f"Subject:Motivation Quotes\n\n{msg}"
                            )


now = dt.datetime.now()
weekday = now.weekday()

test_day = dt.datetime(year=2022, month=2, day=8)
test_weekday = test_day.weekday()

if weekday == 2:
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)
        send_mail(quote)
