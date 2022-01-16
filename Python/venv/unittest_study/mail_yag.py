import yagmail

def send_mail(report,now_time):
    # 邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送账户
    user = '936294813@qq.com'
    # 密码
    password = 'xkcebgvdnrpbbeca'
    # 发件箱
    sender = '936294813@qq.com'
    # 收件箱
    receiver = ['936294813@qq.com','luna.xiao@moritex.com']
    # 邮件主题
    subject='自动化测试结果报告，时间为'+now_time
    #连接邮箱服务器
    yag=yagmail.SMTP(user=user,password=password,host=smtpserver)

    #邮件正文
    content=['你好，今日的自动化测试结果已完成，完成时间为：',now_time]
    yag.send(receiver,subject,content,report)
    print('succes,your mail has send out!')