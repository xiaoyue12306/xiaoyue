import requests,pprint





token='eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5MTU5ODkyODMxNTQ4MzM0MDgiLCJpYXQiOjE2Mzg0MzA0NjMsInN1YiI6IntcImlkXCI6XCI4ODc0MjI4MzgzMzExNTQ0MzJcIixcImFjY291bnRcIjpcIlBBUjAwOTQzNEQwMDAzXCIsXCJhcHBDb2RlXCI6XCJCMjFcIixcInVzZXJGbGFnXCI6MCxcInNuXCI6XCI5MTU5ODkyODMxNDY0NDQ4MDBcIn0iLCJpc3MiOiJjdW53IiwiZXhwIjoxNjM4NTE2ODYzfQ.hYETu5Oz_gTz-Edr-sGxuiTGjdAo-Fsrucu7ptiaw-Y'
headers={"Authorization":"Bearer "+token}

def getListClassSpace():
    # 获取班级圈列表
    params = {'pageNum': '1', 'pageSize': '10', 'userCode': 'TEA073003D0003'}
    listClassSpace = 'https://test.cunwedu.com.cn/teaching-assistant/v1/classSpace/listClassSpace'
    res = requests.get(url=listClassSpace, params=params, headers=headers)
    pprint.pprint(res.json())

# getListClassSpace()

def addComment():
    # 添加评论
    addComment = 'https://test.cunwedu.com.cn/teaching-assistant/v1/classSpace/addComment'
    data = {"sendUserCode": "TEA011609D0003", "id": '', "content": "说的好！", "status": 1, "visibleType": 1,
            "classSpaceId": "915908721465155584"}
    sendComment = requests.get(url=addComment, data=data, headers=headers)
    pprint.pprint(sendComment.json())
# addComment()

def deleteClassSpace():
    # 删除班级圈
    deleteClassSpace = 'https://test.cunwedu.com.cn/teaching-assistant/v1/classSpace/deleteClassSpace'
    data = {'id': '915992325269172224'}
    deleteComment = requests.post(url=deleteClassSpace, data=data, headers=headers)
    pprint.pprint(deleteComment.json())

# deleteClassSpace()