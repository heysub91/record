from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import smtplib
import os


def mail(to, subject, text, attach):
    if not isinstance(to,list):
        to = [to]
    if not isinstance(attach, list):
        attach = [attach]

    gmail_user = '$email_address'
    gmail_pwd = '$pwd'

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = ", ".join(to)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    for file in attach:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename = "%s"' % os.path.basename(file))
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    print('email is sent')
    mailServer.close()


#gmail_user = input('email account: ')
#gmail_pwd = input('password: ')
attach = input('attach: ')
attach = attach.split()

mail('heysub2019@gmail.com', 'Hello From Python', 'Sent with Python', attach)
