import unittest
from time import sleep
from selenium import webdriver


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.url = 'https://b-test.cunwedu.com.cn'
        self.account='17363831767'
        self.password='123456'
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def login_op(self, account, password):
        '''登录操作'''
        self.driver.get(self.url)
        sleep(3)
        self.driver.find_element_by_name('account').clear()
        self.driver.find_element_by_name('account').send_keys(account)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/div[3]/div/button').click()
        sleep(5)

    # def test_a_login(self):
    #     '''登录后检查模块'''
    #     self.login_op(self.account, self.password)
    #     a = self.driver.find_elements_by_class_name('org')
    #     elements = []
    #     for a in a:
    #         elements.append(a.text)
    #     self.assertEqual(elements[0], '教务信息')
    #     self.assertEqual(elements[1], '基本信息')
    #     self.assertEqual(elements[2], '设备管理')
    #     self.assertEqual(elements[3], '健康管理')
    #     self.assertEqual(elements[4], '校园综合分析')
    #     self.assertEqual(elements[5], '消息通知')

    def test_enter_message(self):
        '''进入消息通知模块'''
        self.login_op(self.account, self.password)
        # self.driver.get(self.url)
        sleep(2)
        # self.driver.find_element_by_xpath(
        #     '/html/body/div/div/div[2]/section/div/div[1]/div/div/div/div/div[6]/div/div[1]/img').click()
        # sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div[3]/div[2]/div').text,'管理员')

if __name__ == '__main__':
    unittest.main()
