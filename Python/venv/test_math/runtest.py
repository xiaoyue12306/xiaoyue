import unittest
# import test_add
# import test_sub
# import test_prime
#
#
# suite=unittest.TestSuite()
#
# suite.addTest(test_add.TestAdd("test_add1"))
# suite.addTest(test_add.TestAdd("test_add2"))
#
# suite.addTest(test_sub.TestSub("test_sub1"))
# suite.addTest(test_sub.TestSub("test_sub2"))
#
# suite.addTest(test_prime.TestPrime('test_prime'))
#
# if __name__=='__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)