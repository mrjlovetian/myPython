#! /usr/bin/env python
#coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


#qq邮箱smtp服务器
host_server = 'smtp.exmail.qq.com'
#sender_qq为发件人的qq号码
sender_qq = 'yuhongjiang642.com'
#pwd为qq邮箱的授权码
pwd = 'vin4kUuXT92W4aTj' ## xh**********bdc
#发件人的邮箱
sender_qq_mail = 'yuhongjiang642.com'
#收件人邮箱
receiver = '409360559@qq.com'

#邮件的正文内容
mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
#邮件标题
mail_title = 'Maxsu的邮件'

#ssl登录
smtp = SMTP_SSL(host_server)

#set-debuglevel()用来调试的，参数为1表示启动调试，参数为0关闭调试
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()