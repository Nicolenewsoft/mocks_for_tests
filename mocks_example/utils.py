import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from source import settings

def send_email(emails, subject, body):
    msg = MIMEMultipart()

    message = body

    # setup the parameters of the message
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = ', '.join(emails)
    msg['Subject'] = subject

    print(type(msg['To']))
    print(msg['To'])

    # msg.attach(MIMEText(message, 'html'))
    part1 = MIMEText(message, 'html')

    msg.attach(part1)

    # create server
    server = smtplib.SMTP(settings.EMAIL_HOST + ": " + settings.EMAIL_PORT)

    server.starttls()

    # Login Credentials for sending the mail
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

    # try:
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'].split(","), msg.as_string())

    server.quit()

    return 200