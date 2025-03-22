import smtplib
import datetime as dt

#my_email = "agarwaltushar3710@gmail.com"
#password =  "ohhn vfpe ozih yccf" # chmage this with yahoo password generating
#
#with smtplib.SMTP("smtp.gmail.com") as connection: # this too server
#    connection.starttls()
#    connection.login(user= my_email, password=password )
#    connection.sendmail(
#        from_addr = my_email,
#        to_addrs = "gargtushar138@yahoo.com",
#        msg= "Subject:hello\n\n this is the body of my email"
#    )


now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(now)
print(day_of_week)

date_of_birth = dt.datetime(year= 2005, month=1, day= 5)
print(date_of_birth)