#!/usr/bin/python
#Coding="utf-8"

import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮件
mail_host = "smtp.163.com"
mail_port = 465
mail_user = sys.argv[1]
mail_password = sys.argv[2]
sender = sys.argv[3]
receiver = sys.argv[4]

content = "test"

message = MIMEText(content, 'plain', 'utf-8')
message['From'] = "GitHub Actions<" + sender + ">"
message['To'] = "<" + receiver + ">"

subject = "CSDN Report"
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
    smtpObj.login(mail_user, mail_password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")
