from calculator import Count,Check
import unittest


class TestPrime(unittest.TestCase):
    def setUp(self):
        print('start test')

    def test_prime(self):
        c=Check(3)
        self.assertTrue(c.is_prime(),msg="num is not prime")

    def tearDown(self):
        print('test end')

if __name__ =='__main__':
    unittest.main()