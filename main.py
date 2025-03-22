import smtplib
import datetime as dt
import random

my_email = "agarwaltushar3710@gmail.com"
my_pass = "ohhn vfpe ozih yccf"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("text.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = my_email,
            msg = f"Subject: Monday motivation \n\n {quote}")






# basic knowleadge of the libraries :->


#with smtplib.SMTP("smtp.gmail.com") as connection: # this too server
#    connection.starttls()
#    connection.login(user= my_email, password=password )
#    connection.sendmail(
#        from_addr = my_email,
#        to_addrs = "gargtushar138@yahoo.com",
#        msg= "Subject:hello\n\n this is the body of my email"
#    )


#now = dt.datetime.now()
#day_of_week = now.weekday()
#year = now.year
#print(now)
#print(day_of_week)

#date_of_birth = dt.datetime(year= 2005, month=1, day= 5)
#print(date_of_birth)
