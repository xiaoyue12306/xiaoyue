from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class ClassTest(unittest.TestCase):
    '''优智多课堂测试'''
    def setUp(self):
        self.ffdriver='C:\Program Files\Mozilla Firefox\geckodriver.exe'
        self.driver=webdriver.Firefox(executable_path=self.ffdriver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url='http://test-front-live.cunwedu.com.cn/'

    def test_search(self):
        '''搜索鸭屎课程'''
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('searchContent').clear()
        driver.find_element_by_id('searchContent').send_keys('鸭屎')
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/form/span[2]/i').click()
        time.sleep(4)
        n = driver.window_handles
        driver.switch_to.window(n[1])
        title=driver.title
        self.assertEqual(title,'选课中心−优智多课堂')

    @unittest.skip('跳过这个用例 ')
    def test_skip(self):
        print('i didnot skip')
    def tearDown(self):
        self.driver.quit()

# if __name__=='__main__':
#     unittest.main()
if __name__=='__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(ClassTest('test_search'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='../report/result_' +now+'.html'
    fp=open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='优智多课堂测试报告',
                            description='用例执行情况')
    runner.run(testunit)
    fp.close()