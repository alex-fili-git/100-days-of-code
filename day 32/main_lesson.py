# import smtplib
# # a lot here is very prone to mistakes in strings
# my_email = "emailsenderday32@gmail.com"
# password = ""
#
# # need to specify location
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     # securing connection to email to prevent intervention
#     connection.starttls()
#     # log in
#     connection.login(user=my_email, password=password)
#     # send your mail
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="emailsenderday32@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of email"
#                         )

# import datetime as dt
#
# # get current date
# now = dt.datetime().now()
# # this save attributes which you can use for code
#
# # setting a datetime to specific date
# date_of_birth = dt.datetime(year=1980 , month=01 , day=1)

# import datetime as dt
# import smtplib
# import random
# my_email = "emailsenderday32@gmail.com"
# password = ""
# now = dt.datetime.now()
# if now.weekday() == 0:
#     with open("quotes.txt") as file:
#         quote = random.choice(file.readlines())
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="emailsenderday32@yahoo.com",
#                             msg=f"Subject:Motivation\n\n{quote}")

