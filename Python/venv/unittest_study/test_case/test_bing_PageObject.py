from selenium import webdriver
import unittest
from bing_page_poium import BingPage
from time import sleep
import warnings

class TestBing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        warnings.simplefilter('ignore',ResourceWarning)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_search_a(self):
        page=BingPage(self.driver)
        page.get('https://www.bing.com')
        page.search_input='a'
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title,'a - 国内版 Bing')

if __name__=='__main__':
    unittest.main(verbosity=2)
