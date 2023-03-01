# 倒转数字
# num=12345
# reversed_num=0
# while num>0:
#     reversed_num=reversed_num*10+num%10
#     num//=10
# print(reversed_num)



# 字符串首字母大写 capitalize
# s='i love you      '
# long=len(s)
# did=''
# for i in range(long):
#     if (s[i-1]==' 'and s[i]!=' ')or(i==0 and i!=' '):
#        did=did+s[i].upper()
#     else:did=did+s[i]
# print(did)



# 字符串每个单词反过来 splite
# s='i love you baby'
# print(s.split())
# long=len(s)
# word=''
# l=[]
# num=1
# b=''
# for i in s:
#     if num==long:
#         l.append(word + i+' ')
#     if i!=' ':
#         word=word+i
#         num=num+1
#     if i==' ':
#         l.append(word+i)
#         word=''
#         num=num+1
# print(l)
# ll=len(l)
# for i in range(ll):
#      b=b+l[-i-1]
# print(b.title())




# 字符串每个单词反过来
# s='i love you baby'
# a=s.split()
# b=''
# long= len(a)
# for i in range(long):
#     b=b+a[-i-1]+' '
# print(b.title())



# 寻找水仙花数
# for i in range(100,1000):
#     high=i//100
#     mid=i//10 %10
#     low=i%10
#     if high**3+mid**3+low**3==i:
#         print(i)



# 生成斐波那契数列的前20个数
# num_need=20
# l=[1,1]
# for i in range(1,num_need):
#     a = l[-1]
#     b = l[-2]
#     num=a+b
#     l.append(num)
# print(l)
# 下同
# def fib(n):
#     a, b = 0, 1
#     l=[]
#     for x in range(n):
#         b = a + b
#         a=b-a
#         l.append(a)
#     return l



# 找出10000以内的完美数
# for i in range(1,10000):
#     yz=[]
#     sum=0
#     for x in range(1,i):
#         if i%x==0:yz.append(x)
#     long=len(yz)
#     for a in range(long):
#         sum=sum+yz[a]
#     if sum==i:
#         print(i)

# s='i love you '
# print(sorted(s.split(),key=len))




# import sys
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# f = [x ** 2 for x in range(1, 1000)]
# print(f)
# print(sys.getsizeof(f))
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))



# 元组tuple()  元素不可修改
# t = ('肖越', 25, True, '湖南长沙')
# print(type(t))
# t=list(t)
# t[1]=22
# print(t[1])



#集合set{}
# set1 = set(range(1, 6))
# set2=set(range(3, 6))
# print(set1)
# print(set2)
# print(set1 >= set2)


  
# 字典
# items2 = {num: num ** 2 for num in range(1, 10)}
# print(items2)
# items2[1]=222
# scores = {1: 95, '白元芳': 78, '狄仁杰': 82}
# scores.update( 方启鹤=85)
# print(scores)


# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''
#
# a=get_suffix('aaa.txt',has_dot=True)
# print(a)


"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，
哪些位置是基督徒哪些位置是非基督徒。
"""
# def jdt():
#     l=[i for  i in range(1,31)]
#     print(l)
#     people=len(l)
#     say=0
#     while people>15:
#         if say==8:
#             print(str(l[0]) + '死了')
#             l.pop(0)
#             say=0
#             people=people-1
#         else:
#             say=say+1
#             l.append(l[0])
#             l.pop(0)
#
#
#     print('目前剩余：'+str(people)+'人')
#     print('他们活了下来：',l)
#
# if __name__=='__main__':
#     jdt()

import os


# a = 0
# b = 1
# for _ in range(10):
#     a, b = b, a + b
#     print(a,end=' ')

# num_need=10 #需要前多少项
# l=[1,1]
# for i in range(1,num_need-1):
#     a = l[-1]
#     b = l[-2]
#     num=a+b
#     l.append(num)
# print(l)


