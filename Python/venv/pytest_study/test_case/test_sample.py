import pytest
def add_one(x):
    return x+1


def test_add_one():
    assert add_one(1)==2


if  __name__=='__main__':
    pytest.main()