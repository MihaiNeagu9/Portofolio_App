import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "emailtest09999@gmail.com"
password = "ozvo bmpq veve gmug"

receiver = "emailtest09999@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)