# -*- coding:utf-8 -*-
'''
    方法
    实现一个叫myPop()的函数,功能类似于列表的pop()方法,
    用一个列表作为输入, 移除列表的最新一个元素,并返回它。
'''

def myPop(myList):
    data = myList[-1]
    myList.remove(data)
    return data

myList = [1, 2, 3, 4, 5]
data = myPop(myList)
print data, myList
