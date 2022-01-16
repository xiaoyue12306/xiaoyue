from base import Base
from poium import Page, Element


# class BingPage(Base):
#     url = 'https://www.bing.com'
#
#     def search_input(self, search_key):
#         self.by_id('sb_form_q').send_keys(search_key)
#
#     def search_button(self):
#         self.by_id('search_icon').click()

class BingPage(Page):
    '''使用poium'''
    search_input = Element(id_='sb_form_q',timeout=5,describe='输入框')
    search_button = Element(id_='search_icon',describe='搜索按钮')


'''
poium 的文档地址：https://github.com/SeldomQA/poium
poium支持的定位方式
elem_id = PageElement(id_='id')
elem_name = PageElement(name='name')
elem_class = PageElement(class_name='class')
elem_tag = PageElement(tag='input')
elem_link_text = PageElement(link_text='this_is_link')
elem_partial_link_text = PageElement(partial_link_text='is_link')
elem_xpath = PageElement(xpath='//*[@id="kk"]')
elem_css = PageElement(css='#id')
'''