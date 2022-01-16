import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares =[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

#设置表标题和XY轴标题
plt.title('Squares Number',fontsize=24)
plt.xlabel('Value',fontsize=18,color='gold')
plt.ylabel('Squares',fontsize=18,color='gold')

# 设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)

# 绘制单个点
plt.scatter(2,8)

plt.show()