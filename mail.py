#!/usr/bin/python

import smtplib
import time
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.MIMEMultipart import MIMEMultipart

if __name__ == "__main__":
sender = 'sender email id'
receivers = ['reciver']
now = time.strftime("%c")
msg = MIMEMultipart()
msg['Subject'] = 'Test time now is %s' %now
msg['From'] = sender
msg['To'] = ', '.join(receivers)
body = "Test time now is %s" %now
msg.attach(MIMEText(body, 'plain'))
try:
   smtpObj = smtplib.SMTP('mail.relay.server', port)
   smtpObj.sendmail(sender, receivers, msg.as_string())
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
