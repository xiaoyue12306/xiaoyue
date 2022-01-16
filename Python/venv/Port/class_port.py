import requests


login_url='http://test-front-live.cunwedu.com.cn/login'
data={'account':'17363831766',
      'password':'4746e4ad214ab82861324cf3e6a9ffa983dd56ceb381c215f4ff79af9e3b121576d02a4f1c0ec14f70cf236a0bfbbe785087b688bd27f51ace717bdd84eb56ab5cd7998d0119dcc3d6a022cb1da583f900feffbabade3c2baa0e6e24e26dbf9eb22e01688e1582ba5d7be30082296c07211ba705346d00d91ae31710fa370011',
      'remeberMe':'false',
      'type':'1'
      }

login=requests.post(url=login_url,data=data)
print(login.json())
print(login.cookies)

# 修改名称
change_name_url='http://test-front-live.cunwedu.com.cn/student/updateBaseInfo'
change_data={
      'id':'3052172',
      'nickName':'湘湘',
      'sex'	:'MALE',
      'age'	:'100',
      'userSign':'新云网测试部买水财务总监'
}
change=requests.post(url=change_name_url,data=change_data,cookies=login.cookies)
print(change)


login_url='http://test-front-live.cunwedu.com.cn/login'
data={'account':'17363831766',
      'password':'4746e4ad214ab82861324cf3e6a9ffa983dd56ceb381c215f4ff79af9e3b121576d02a4f1c0ec14f70cf236a0bfbbe785087b688bd27f51ace717bdd84eb56ab5cd7998d0119dcc3d6a022cb1da583f900feffbabade3c2baa0e6e24e26dbf9eb22e01688e1582ba5d7be30082296c07211ba705346d00d91ae31710fa370011',
      'remeberMe':'false',
      'type':'1'
      }

login=requests.post(url=login_url,data=data)
print(login.json()['user']['nickName'])