import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#邮箱服务器
smtpserver = 'smtp.qq.com'
#发送账户
user = '936294813@qq.com'
#密码
password = 'xkcebgvdnrpbbeca'
#发件箱
sender = '936294813@qq.com'
#收件箱
receiver = '936294813@qq.com'
#邮件主题
subject = 'hello yy'

# 发送的邮件
with open('csv_data/bing_data.csv') as file:
    attachment=file.read()
att=MIMEText(attachment,'text','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="bing_data.csv"'

msg=MIMEMultipart()
msg['Subject']=subject
msg.attach(att)


def send_mail():
    # 发送
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('发送成功')

send_mail()