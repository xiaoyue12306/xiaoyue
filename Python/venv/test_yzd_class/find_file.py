import os

report_path=r'C:\Users\xyy\Desktop\xy\Python\venv\test_yzd_class\report'
lists=os.listdir(report_path)
print(lists)
lists.sort(key=lambda fn: os.path.getmtime(report_path+"\\"+fn))
print(('最新文件为：'+lists[-1]))
file = os.path.join(report_path, lists[-1])
print(file)