# -*- coding:utf-8 -*-

'''
    Fibonacci数列.
    Fibonacci数列形如1, 1, 2, 3, 5, 8, 13, 21等等.
    也就是说,下一个值是序列中前两个值之和.
    写一个函数,给定N,返回第N个Fibonacci数字.
    例如,第1个Fibonacci数字是1,第6个是8.
'''

a = [1, 1]
def Fibonacci(x):
    while x-2:
        sum = 0
        for num in a[-2:]:
            sum += num
        a.append(sum)
        x -= 1
    return a[-1]

# 爱上我自己!
