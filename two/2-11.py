# -*- coding:utf-8 -*-

'''
	带文本菜单的程序
	写一个带文本菜单的程序,菜单项如下
	(1)取五个数的和
	(2)取五个数的平均值....(X)退出。
	由用户做一个选择,然后执行相应的功能。当用户选择退出时程序结束。
	这个程序的有用之处在于用户在功能之间切换不需要一遍一遍的重新启动你的脚本。(这对开发人员测试自己的程序也会大有用处）
'''

# split()函数：返回分隔后的字符串列表
# str.split(str='',num=string.count(str)) 默认已空格分隔字符串

while True:
	sum = 0
	average = 0
	num = raw_input('请输入五个数字,以空格键分开\n')
	list = num.split()
	q = raw_input('输入1选择求五个数的和\n输入2选择求五个数的平均值\n输入x选择退出\n')
	if q.lower() == '1':
		for x in list:
			sum += int(x)
		print '这五个数的和是%d' % sum
	elif q.lower() == '2':
		for x in list:
			sum += int(x)
			average = float(sum)/5
		print '这五个数的平均值是%f' % average
	elif q.lower() == 'x':
		break

