import unittest
from calculator import Calculator


def setUpModule():
    pass


def tearDownModule():
    pass


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        c = Calculator(1, 1)
        result = c.add()
        self.assertEqual(result, 2)

    def test_sub(self):
        c = Calculator(1, 1)
        result = c.sub()
        self.assertEqual(result, 0)

    def test_mul(self):
        c = Calculator(1, 1)
        result = c.mul()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()  # 按照测试类、方法的名称来执行用例
    # suit=unittest.TestSuite()
    # suit.addTest(TestCalculator('test_add'))
    # suit.addTest(TestCalculator('test_sub'))
    # runner=unittest.TextTestRunner()
    # runner.run(suit)
