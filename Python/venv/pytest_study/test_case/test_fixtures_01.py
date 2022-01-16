import pytest



def multiply(a, b):
    return a * b

class TestMultilpyy:
    @classmethod
    def setup_class(cls):
        print('\nclass start')
    @classmethod
    def teardown_class(cls):\
        print('\nclass close')
    def setup_method(self,method):
        print('method start')
    def teardown_method(self,method):
        print('method close')
    def setup(self):
        print('start')
    def teardown(self):
        print('close')
    def test_multiply1(self):
        print('\ntest1!!!!!!!!!!!!!!!!!!!!!')
        assert multiply(1,1)==1
    def test_multiply2(self):
        print('\ntest2!!!!!!!!!!!!!!!')
        assert multiply(2,2)==4

if __name__=='__main__':
    pytest.main()