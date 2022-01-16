import unittest
from selenium import webdriver
from time import sleep


# @unittest.skip('跳过的用例')
class TestBing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # self.FireFoxDriver =
        # self.driver = webdriver.Firefox(executable_path=self.FireFoxDriver)
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def bing_search_op(self, keyword):
        '''bing搜索操作'''
        url = 'https://www.bing.com'
        self.driver.get(url)
        self.driver.find_element_by_id('sb_form_q').clear()
        self.driver.find_element_by_id('sb_form_q').send_keys(keyword)
        self.driver.find_element_by_id('search_icon').click()
        sleep(2)

    def test_search_lol(self):
        '''测试bing搜索关键词lol ，检查title'''
        search_key = 'lol'
        self.bing_search_op(search_key)
        self.assertEqual(self.driver.title, search_key + ' - 国内版 Bing')

    def test_search_what_is_love(self):
        '''测试bing搜索关键词what is love ，检查title'''
        search_key = 'what is love'
        self.bing_search_op(search_key)
        self.assertEqual(self.driver.title, search_key + ' - 国内版 Bing')


if __name__ == '__main__':
    unittest.main()
