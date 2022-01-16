# from btest_poium import Btest as ele

# class TestLogin(ele):
#     def a(self):
#         pass
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