import unittest, time, os
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(file_new, now):
    smtpserver = 'smtp.qq.com'
    user = '936294813@qq.com'
    password = 'xkcebgvdnrpbbeca'
    sender = '936294813@qq.com'
    receiver = '936294813@qq.com'

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('优智多课堂自动化测试报告' + now, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("优智多课堂测试报告已发送至:" + receiver)


# 找到最新的测试报告
def new_report(test_report):
    lists = os.listdir(test_report)
    print(lists)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))
    print(('最新文件为：' + lists[-1]))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    test_dir = './test_case'
    test_report = './report'
    discover = unittest.defaultTestLoader.discover(test_dir, 'test_*.py')
    filename = './report/result_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='优智多课堂PC端测试报告' + now, description='用例执行情况')
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report, now)
