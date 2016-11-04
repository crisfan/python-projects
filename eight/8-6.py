# -*- coding:utf-8 -*-

'''
    素因子分解
    以刚才练习中的isprime()和getfactors()函数为基础编写一个函数,
    它接受一个整数作为参数,返回该整数所有素数因子的列表。
    这个过程叫做求素因子分解,它输出的所有因子之积应该是原来的数字。
    注意列表里可能有重复的元素例如输入20,返回结果应该是[2, 2, 5]
'''


def isprime(prime):
    x = prime / 2
    for i in range(x, 1, -1):
        if prime % i == 0:
            return False
    else:
        return True


def getfactors(x):
    Arr = []
    for i in range(2, x+1):
        if x % i == 0 and isprime(i):
            Arr.append(i)
    else:
        return Arr


def findPrimeFactory(number):
    temp = getfactors(number)
    k = 1
    for i in temp: k = k * i
    if k == number:
        return temp
    else:
        j = number / k
        return temp + findPrimeFactory(j)


arr = findPrimeFactory(20)
print sorted(arr)
