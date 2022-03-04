import requests
from pprint import pprint

r = requests.get('https://api.github.com/events',stream=True)

pprint(r.encoding)
# pprint(r.json())
# #要访问原始相应，则必须在初始请求中设置了stream=True
print(r.raw.read(10))
#  httpbin.org/get?key=val


# #可以以字符字典来传参数

# payload = {'key': 'value', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
# pprint(r.url)
#
# payload2 = {'key': 'value', 'key2': ['value2', 'value3']}
# r = requests.get('https://httpbin.org/get', params=payload2)
# pprint(r.url)


#post
