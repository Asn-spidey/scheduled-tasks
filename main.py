# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

from datetime import datetime as dt
import pandas
import random
import smtplib
from collections import defaultdict
import os

today = (dt.now().month, dt.now().day)

data = pandas.read_csv("birthdays.csv")

bday_dict = defaultdict(list)

for (index, row) in data.iterrows():
    key = (row.month, row.day)
    bday_dict[key].append(row)

if today in bday_dict:
    person = bday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,1)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person[0]["name"])

    with smtplib.SMTP("smtp.mail.me.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person[0]["email"],
            msg=(
                f"From: {my_email}\n"
                f"Subject: Happy {dt.now().year - person[0]["year"]}th Birthday!\n"
                f"{contents}"
            )
        )
