# -*- coding:utf-8 -*-

'''
    循环和运算符
    创建一个包含五个固定数值的列表或元组，输出他们的平均值。本练习的难点之一是通过除法得到平均值。
    你会发现整数除会截去小数，因此你必须使用浮点除以得到更精确的结果。
    float()内建函数可以帮助你实现这一功能。
'''

# float()用法,和int()大同小异
arr =[1,2,3,4,6]
len = len(arr)
i, sum = 0, 0
while i<len:
    sum += arr[i]
    i += 1

averge = float(sum)/len
print 'averge is',averge