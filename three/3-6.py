# -*- coding:utf-8 -*-

'''
	变量赋值。
	（a）赋值语句x, y, z = 1, 2, 3会在x、y、z中分别赋什么值？
	（b）执行z, x, y = y, z, x后，x、y、z中分别含有什么值？
'''

#(a)
# 赋值语句x,y,z中分别为1，2，3

#(b)
# 执行后，x,y,z分别为3，1，2

x,y,z = 1,2,3
print x,y,z
z,x,y = y,z,x
print x,y,z