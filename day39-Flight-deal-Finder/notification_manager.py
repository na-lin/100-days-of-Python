import requests
import os
from twilio.rest import Client
import smtplib

MY_EMAIL = "auteforpt@yahoo.com"
MY_PASSWORD = "oidfpmzpbrbbvgdz"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message):
        self.message = message

    def send_sms(self):
        account_sid = "AC533ce877dd8c0c2ed97afdf136833441"
        auth_token = "9e55c738bcb90897e584c6c8311f73ec"
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=self.message,
            from_='+18456689981',
            to='+16463318838'
        )

        # print(message.sid)

    def send_email(self, to_address, message):
        for email in to_address:
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,
                                    msg=f'Subject:New Flight Deal\n\n{message}'.encode('utf-8'))
