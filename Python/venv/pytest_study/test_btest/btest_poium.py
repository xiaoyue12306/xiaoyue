from poium import Page,Element

class Btest(Page):
    username_input=Element(css='html body div#app div.login-content div.content div.login-box'
                               ' div.login-right div.login-messege div.demo-input-suffix '
                               'div.input.el-input input.el-input__inner')
    password_input=Element(type_name='password')
    login_button=Element(class_name='blue-btn')













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