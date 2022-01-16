import requests,pprint

# login_url='https://test.cunwedu.com.cn/area-oa/fillthefrom/fillInReportDetail/v1/savebatchwholenetwork'
# data={{"formId":"1432886662840586240","fillInReportDetails":[{"questionnaireFormDetailId":"1432886662882529280","answer":"1"},{"questionnaireFormDetailId":"1432886662886723584","answer":"哈哈哈"},{"questionnaireFormDetailId":"1432886662886723585","answer":"2021-09-01T02:33:28.000Z"}]}}
#
# login=requests.post(url=login_url,data=data)
# print(login)


# 登录
login_url="https://test.cunwedu.com.cn/area-oa/front/auth?tenantId="
data={"username":"17363831767","password":"E10ADC3949BA59ABBE56E057F20F883E"}
login=requests.post(url=login_url,json=data)
token=login.json()['token']
headers={"Authorization":"Bearer "+token}
# 获取系统通知
# headers={"Authorization":"Bearer "+token}
# get_system_notic='https://test.cunwedu.com.cn/area-oa/api/message/v1/getSystemNoticeList'
# data1={"receiveCode":"STA000605D0003","pageSize":7,"pageNum":1}
# data2={"receiveCode":"STA002406D0003","pageSize":7,"pageNum":1}
# data3={"receiveCode":"STA000631D0003","pageSize":7,"pageNum":1}
# system_notic=requests.post(url=get_system_notic,json=data1,headers=headers)
# pprint.pprint(system_notic.json())

# 获取私信通知列表
# getPrivateMessageUnreadList="https://test.cunwedu.com.cn/area-oa/api/message/v1/getPrivateMessageUnreadList"
# data1={"receiveCode":"STA000605D0003","pageSize":7,"pageNum":1}
# data2={"receiveCode":"STA002406D0003","pageSize":7,"pageNum":1}
# data3={"receiveCode":"STA000631D0003","pageSize":7,"pageNum":1}
# res=requests.post(url=getPrivateMessageUnreadList,json=data3,headers=headers)
# pprint.pprint(res.json())

# 获取私信详情
getPrivateMessageDetailList="https://test.cunwedu.com.cn/area-oa/api/message/v1/getPrivateMessageDetailList"
data1={"receiveCode":"STA002416D0003","sendCode":"STA002801D0003","pageSize":7,"pageNum":1}
res=requests.post(url=getPrivateMessageDetailList,json=data1,headers=headers)
pprint.pprint(res.json())