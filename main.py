import smtplib

my_email = "agarwaltushar3710@gmail.com"
password =  "ohhn vfpe ozih yccf"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password )
    connection.sendmail(
        from_addr = my_email,
        to_addrs = "gargtushar138@yahoo.com",
        msg= "Subject:hello\n\n this is the body of my email"
    )
