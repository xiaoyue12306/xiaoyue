import unittest

class TestSecond(unittest.TestCase):
    # @unittest.skip('跳过的用例')
    def test_se(self):
        self.assertEqual(1,1)