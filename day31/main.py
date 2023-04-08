##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# --------------------------------MY CODE----------------------------------#
import datetime as dt
import pandas
import random
import smtplib

LETTER = ["letter_1.txt", "letter_2.txt", "letter_2.txt"]
MY_EMAIL = "auteforpt@yahoo.com"
PASSWORD = "uunaoprbuwckqzyx"


def send_email(email, msg):
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject: Happy Birthday\n\n{msg}"
                            )


# todo get current month and day
now = dt.datetime.now()
now_month = now.month
now_day = now.day
# todo: read infor from birthday.csv
original_data = pandas.read_csv("birthdays.csv")
birthday = original_data.to_dict(orient="records")
# todo: comapre whether current datatime == a person's month and day
for infor in birthday:
    if infor["month"] == now_month and infor["day"] == now_day:
        birthday_person_name = infor["name"]
        birthday_person_email = infor["email"]
        # todo: randomly select a letter txt
        with open(f"./letter_templates/{random.choice(LETTER)}") as temp:
            # content = temp.readlines()
            # todo: if don't want to create another file,just use under 3 line code.
            old_content = temp.read()
            new_content = old_content.replace("[NAME]", birthday_person_name)
            send_email(birthday_person_email, new_content)

        # # todo: replace[] into the person's name and write into new txt file
        # with open(f"./birthday_wisher/letter_for_{birthday_person_name}", mode="w") as letter:
        #     for line in content:
        #         if "[NAME]" not in line:
        #             letter.write(line)
        #         else:
        #             letter.write(line.replace("[NAME]", birthday_person_name))
        # # todo: send to the person's email
        # with open(f"./birthday_wisher/letter_for_{birthday_person_name}") as letter:
        #     content = letter.read()
        #     send_email(birthday_person_email, content)
