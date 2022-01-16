import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.qq.com'
user='936294813@qq.com'
password='xkcebgvdnrpbbeca'
sender='936294813@qq.com'
receiver='936294813@qq.com'
subject='hello yy'

sendfile=open(r'C:\Users\xyy\Desktop\xy\Python\venv\test_yzd_class\report\result_2021-08-21 15_56_57.html').read()

att=MIMEText(sendfile,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="log.txt"'
msg=MIMEText('<html><h1>你好呀</h1></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')

smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()