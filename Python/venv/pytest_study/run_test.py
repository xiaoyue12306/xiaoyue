import pytest, time

if __name__ == '__main__':
    '''运行 & 生成报告'''
    test_dir = './test_case'
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')

    #运行并生成XML格式报告
    # report_name = './report/' + now_time + 'result.xml'
    # pytest.main(['-s', test_dir, '--junit-xml=' + report_name])

    #运行并生成在线测试报告
    # pytest.main([test_dir,'--pastebin=all'])

    #运行并成HTML测试报告,失败重跑3次
    report_name = './report/' + now_time + 'result.html'
    pytest.main(['-v','--html='+report_name,'--reruns','3'])

    #运行所有
    # pytest.main(['-s'])

    #parallel多线程运行
    # pytest.main(['./test_case/test_parallel.py','--test-per-worker','auto'])