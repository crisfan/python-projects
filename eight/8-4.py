# -*- coding:utf-8 -*-

'''
    素数
    我们在本章已经给出了一些代码来确定一个数字的最大约数或者它是否是一个素数。
    请把相关代码转换为一个返回值为布尔值的函数,函数名为isprime()。
    如果输入的是一个素数,那么返回True,否则返回False。
'''


def isprime(prime):
    x = prime / 2
    for i in range(x, 1, -1):
        if prime % i == 0:
            return False
    else:
        return True

print isprime(4)


