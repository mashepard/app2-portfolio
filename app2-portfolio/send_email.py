import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "mshepard1963@gmail.com"
password = "bglllajyvwfyejcb"

receiver = "mshepard1963@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Test Message
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)