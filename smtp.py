from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

#输入口令
from_add = input('From: ')
password = input('Password: ')

#输入收件人地址
to_address = input('To: ')

#输入服务器地址
smtp_server = input('STMP: ')

import smtplib
server = smtplib.SMTP(smtp_server, 23)#SMTP协议默认端口号是25
server.set_debuglevel(1)
server.login(from_add, password)
server.sendmail(from_add, [to_address], msg.as_string())
server.quit()