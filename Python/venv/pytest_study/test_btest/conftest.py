import pytest
from selenium import webdriver
#设置浏览器驱动
driver_type='firefox'

#设置URL
url='https://b-test.cunwedu.com.cn'

#设置失败重跑次数
rerun='3'

#设置测试用例的目录
cases_path='./'

@pytest.fixture(scope='session', autouse=True)
def browser_start():
    global driver
    if driver_type == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise NameError('driver驱动定义错误或暂未配置！')

@pytest.fixture(scope='session', autouse=True)
def browser_close():
    yield driver
    driver.close()
    print('test end!')