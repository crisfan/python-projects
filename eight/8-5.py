# -*- coding:utf-8 -*-


'''
    约数
    完成一个名为getfactors()的函数。
    它接受一个整数作为参数,返回它所有约数的列表,包括1和它本身。
'''


def getfactors(x):
    Arr = []
    for i in range(1, x+1):
        if x % i == 0:
            Arr.append(i)
    else:
        return Arr

print getfactors(2)
