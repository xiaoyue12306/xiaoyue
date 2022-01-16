import unittest
from calculator import Count

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("Test Start")

    def test_add1(self):
        j=Count(1,2)
        self.assertEqual(j.add(),3,msg='1+2运算错误')

    def test_add2(self):
        j=Count(2,2)
        self.assertEqual(j.add(),4,msg='2+2运算错误')

    def tearDown(self):
        print("Test End")

if __name__=='__main__':
    unittest.main()
