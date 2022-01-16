import pytest


def add(a, b):
    return a + b


# 判断是否为素数
def is_prime(c):
    if c < 1:
        return False
    for i in range(1, c):
        if c % i == 0:
            return False
        return True


# 测试相等
def test_add_1():
    assert add(1, 1) == 2


# 测试不相等
def test_add_2():
    assert add(1, 2) != 2


# 测试大于等于
def test_add_3():
    assert add(1, 2) >= 2


# 测试小于等于
def test_add_4():
    assert add(1, 2) <= 4


# 测试包含
def test_in_1():
    a = 'he'
    b = 'hello'
    assert a in b


# 测试不包含
def test_in_2():
    a = 'hi'
    b = 'hello'
    assert a not in b


# 判断是否为True
def test_is_prime_not_true_1():
    assert not is_prime(2)


# 判断是否不为True
def test_is_prime_not_true_2():
    assert is_prime(2) is not True


# 判断是否不为True
def test_is_prime_not_true_3():
    assert not is_prime(2)


# 判断是否为False
def test_is_prime_not_true_4():
    assert is_prime(2) is False


if __name__ == '__main__':
    pytest.main()
