import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = os.getenv('gaaku_email')
password = os.getenv('gaaku_pwd')


def send(domain, userid, email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    print('Logged in')
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = email
    message['Subject'] = "GaaKU - Confirm your email"
    
    body = f"""
            Please follow the link below to confirm your account.
            http://{domain}/confirm/{userid}
            Thank you!
    """
    message.attach(MIMEText(body, 'html'))
    server.send_message(message)
    print('Email sent to', email)