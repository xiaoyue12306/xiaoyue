import csv, unittest, codecs
from itertools import islice
from selenium import webdriver
from time import sleep


class TestBing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.test_search_keys = []
        with codecs.open(r'C:\Users\xyy\Desktop\xy\Python\venv\unittest_study\csv_data\bing_data.csv','r', encoding='utf-8') as file:
            data = csv.reader(file)
            for line in islice(data, 1, None):
                self.test_search_keys.append(line)
        print(self.test_search_keys)
        file.close()

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

    def test_search_a(self):
        '''测试bing搜索bing_data.csv的数据，检查title'''
        self.bing_search_op(self.test_search_keys[0][1])
        self.assertEqual(self.driver.title, self.test_search_keys[0][1] + ' - 国内版 Bing')

    def test_search_b(self):
        '''测试bing搜索bing_data.csv的数据，检查title'''
        self.bing_search_op(self.test_search_keys[1][1])
        self.assertEqual(self.driver.title, self.test_search_keys[1][1] + ' - 国内版 Bing')

    def test_search_c(self):
        '''测试bing搜索bing_data.csv的数据，检查title'''
        self.bing_search_op(self.test_search_keys[2][1])
        self.assertEqual(self.driver.title, self.test_search_keys[2][1] + ' - 国内版 Bing')


if __name__ == '__main__':
    unittest.main()
