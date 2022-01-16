from matplotlib import pyplot as plt
from random_walk import RandomWalk



# point_num=input('请输入随机模拟点数量:')
rw=RandomWalk()
rw.do_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()