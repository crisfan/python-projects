# -*- coding:utf-8 -*-

'''
    阶乘.
    一个数的阶乘被定义为从1到该数字所有数字的乘积.
    N的阶乘简写为N!. 写一个函数, 指定N, 返回N!的值.
'''


def factorial(x):
    sum = 1
    if x == 0:
        return sum
    else:
        for i in range(1, x+1):
            sum *= i
        return sum

