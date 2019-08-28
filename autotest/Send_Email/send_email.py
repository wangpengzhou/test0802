# coding:utf-8
import  smtplib
from  email.mime.text import MIMEText   #定义内容
from email.header import  Header  #定义标题

smptserver = 'smtp.163.com'  # 服务器名

user='1362924308@163.com' #登录邮箱
password='198810wpz'# 授权码

sender='1362924308@163.com' #发件人
receieve = '1362924308@163.com' #收件人

subject = 'web selenium 测试报告' #邮件标题
content = '<html><h1 style = "color :red">我要自学网</h1></html>'#邮件内容

msg = MIMEText(content,'html','utf-8') #标题和邮件的装载
msg['Subject']= Header(subject,'utf-8')
msg['From']='1362924308@163.com'
msg['To']='1362924308@163.com'

smtp = smtplib.SMTP_SSL(smptserver,994)
print(smtp)
smtp.helo(smptserver)  #向服务器发送认证
smtp.ehlo(smptserver) #得到响应
smtp.login(user,password)
# print('start send email...')
# smtp.sendmail(sender,receieve,msg.as_string())
# smtp.quit()
# print('send email finished')