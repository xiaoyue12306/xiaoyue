import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt,data,file_data,unpack

@ddt
class TestBing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
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

    @data(['case1','a'],['case2','b'],['case3','c'])
    #也可使用元组或字典 （）{}
    @unpack
    def test_search(self,case,search_key):
        '''ddt参数化测试'''
        self.bing_search_op(search_key)
        self.assertEqual(self.driver.title,search_key+' - 国内版 Bing')

    @file_data('../csv_data/ddt_data.json')
    def test_search_json(self,search_key):
        '''ddt json'''
        self.bing_search_op(search_key)
        self.assertEqual(self.driver.title,search_key+' - 国内版 Bing')



if __name__ == '__main__':
    unittest.main(verbosity=2)
