import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from mail_yag import send_mail


if __name__ == '__main__':
    '''生成HTML格式的报告'''
    test_dir = './test_case'
    suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*', top_level_dir=None)
    now_time=time.strftime('%Y-%m-%d %H_%M_%S')
    html_report='./report/'+now_time+'result.html'
    fp=open(html_report,'wb')
    runner=HTMLTestRunner(stream=fp,
                          verbosity=2,
                          title='新云网智慧教务管理平台自动化测试报告',
                          description='运行环境：Windows11,FireFox浏览器')
    # runner = unittest.TextTestRunner()
    runner.run(suits)
    fp.close()
    send_mail(html_report,now_time)
