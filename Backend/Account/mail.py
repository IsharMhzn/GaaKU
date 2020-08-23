import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'gaakuapp@gmail.com'
password = 'gaaku4admins'


def send(domain, userid, email, type):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    print('Logged in')
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = email
    if type == 'confirm':
        message['Subject'] = "GaaKU - Confirm your email"
    else:
        message['Subject'] = "GaaKU - Password Reset for your account"

    body = f"""
            Please follow the link below to confirm your account.
            http://{domain}/{type}/{userid}
            Thank you!
    """
    message.attach(MIMEText(body, 'html'))
    server.send_message(message)
    print('Email sent to', email)
