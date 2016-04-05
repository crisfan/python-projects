# -*-coding:utf-8 -*-

'''
	元素排序
	(a)让用户输入三个数值并将分别将它们保存到3个不同的变量中。
 	   不使用列表或排序算法, 自己写代码来对这三个数由小到大排序。
 	(b)修改(a)的解决方案,使之从大到小排序
'''

# 借助别人的思想(想不出来-_-!)	

a = raw_input('请输入一个值\n')
b = raw_input('请输入一个值\n')
c = raw_input('请输入一个值\n')
maxNum = max([a,b,c])
minNum = min([a,b,c])
mid = [x for x in [a,b,c] if x!=minNum and x!=maxNum]
print minNum,mid[0],maxNum
print maxNum,mid[0],minNum