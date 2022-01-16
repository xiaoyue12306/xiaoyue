import matplotlib.pyplot as plt


x_value=list(range(1,100))
y_value=[x**2 for x in x_value]
plt.scatter(x_value,y_value,s=50,edgecolors='none',c=y_value,cmap=plt.cm.Blues)
plt.axis=([0,1000,0,10000])
# 设置表样式
plt.title('Squares Number',fontsize=24)
plt.xlabel('Value',fontsize=18,color='gold')
plt.ylabel('Squares',fontsize=18,color='gold')

# 设置刻度的大小
plt.tick_params(axis='both',width=2,which='major',labelsize=18,color='red')
# plt.show()
plt.savefig('my_first_fig')