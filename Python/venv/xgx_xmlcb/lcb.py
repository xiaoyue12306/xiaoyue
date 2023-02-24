import datetime
scheduled_start_date=input('请输入计划开始时间：')
scheduled_end_date=input('请输入计划结束时间：')
actual_start_date=input('请输入实际开始时间：')
actual_end_date=input('请输入实际结束时间：')
scheduled_date=((datetime.datetime.strptime(scheduled_end_date, "%Y.%m.%d").date())-(datetime.datetime.strptime(scheduled_start_date, "%Y.%m.%d").date())).days
print('计划用时共：'+str(scheduled_date)+'天')
actual_date=((datetime.datetime.strptime(actual_end_date, "%Y.%m.%d").date())-(datetime.datetime.strptime(actual_start_date, "%Y.%m.%d").date())).days
print('实际用时共：'+str(actual_date)+'天')
pcl=(actual_date-scheduled_date)/scheduled_date
print('该项目偏差率为：'+str(pcl*100)+'%')
# print('该项目偏差率为：{:.2f}%'.format(pcl))
# print(pcl)
status=''
if pcl<-0.1:
    status='超前'
elif 0.2>pcl>=0.1:
    status='滞后'
elif pcl >= 0.2:
    status = '较大滞后'
elif 0.1>=pcl >= -0.1:
    status = '相符'
print('该项目当前状态为：'+status)