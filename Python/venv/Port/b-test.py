import requests
import pprint

token='eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5MjE0NTI1NDE3NjEzMDI1MjgiLCJpYXQiOjE2Mzk3MzMwMDUsInN1YiI6IntcImlkXCI6XCI5NTI4XCIsXCJhY2NvdW50XCI6XCJzaGVuZ3RpbmdcIixcImFwcENvZGVcIjpcIkEwM1wiLFwidXNlckZsYWdcIjowLFwic25cIjpcIjkyMTQ1MjU0MTMzMzQ4MzUyMFwifSIsImlzcyI6ImN1bnciLCJleHAiOjE2Mzk4MTk0MDV9.LWFONBT6kiyL_Ai4QhOlSAi0F5lby5DOmIp5wgE5_s0'
headers={"Authorization":"Bearer "+token}
def add_class_room(number):
    '''b-test,添加教室'''
    url='https://test.cunwedu.com.cn/backend/bm/schoolrooms/'
    data={"name":number,"remark":"清华大学的教室","floorName":1,"schoolCode":"ORG000362D0003","roomTypeId":"855396596433686528","buildingId":"855396511322869760"}
    res = requests.post(url=url, json=data, headers=headers)
    # pprint.pprint(res.json())
    print('.')


list=range(206,299)
for i in list:
    add_class_room(i)





