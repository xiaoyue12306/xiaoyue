import selenium


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url=None):
        # 打开页面
        if url==None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self, id):
        # id定位
        return  self.driver.find_element_by_id(id)

    def by_name(self, name):
        # name定位
        return  self.driver.find_element_by_name(name)

    def by_class(self, class_name):
        # class定位
        return  self.driver.find_element_by_class_name(class_name)

    def by_xpath(self, xpath):
        # xpath定位
        return  self.driver.find_element_by_xpath(xpath)

    def get_text(self, xpath):
        # 获取text
        return self.by_xpath(xpath).text

    def get_title(self):
        # 获取title
        return self.driver.title

    def js(self, script):
        # 执行js脚本
        self.driver.execute_scripts(script)
