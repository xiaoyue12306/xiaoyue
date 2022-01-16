import requests, json
from pprint import pprint
import re

def readline():
    idtxt=open('id.txt')
    nums=idtxt.readlines()
    print(nums)
    return nums

def writenull(null_id):
    write=open('null.txt','a')
    write.write(null_id)
    write.close()

def login(name='chenbo',pwd='123456'):
    login_url = 'http://114.115.142.136:8090/teachers/auth/login'
    login_account = {'loginName':name,
                     'password':pwd}
    login = requests.post(url=login_url, data=login_account)
    # print(login.json()['data']['accessToken'])
    return (login.json()['data']['accessToken'])


def get_question():
    # 查看题目
    logtoken=str(login())
    nums=readline()
    write = open('null.txt', 'a')
    for num in nums:
        num=num[:8]
        question_url = 'http://114.115.249.183:8091/v1/resource/mainquestions/'+num
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'authorization':'Bearer'+logtoken}
        get_question_page = requests.get(url=question_url, headers=headers)
        # pprint(get_question_page.text)
        # print(question_url)
        pattern = re.compile('http://cunw-edu-statics-test')
        strr = get_question_page.text
        # print('----------------分割线------------------------------------------')
        # print(pattern.search(strr))
        if pattern.search(strr) == None:
            print(num+'没有找到地址')
            write.write(num+'\r\n')
            # writenull()
        # print('----------------分割线------------------------------------------')

get_question()