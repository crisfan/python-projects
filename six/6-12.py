# -*- coding:utf-8 -*-

'''
    字符串
    (a) 创建一个名字为findchr()的函数,函数声明如下:
        def findchr(string, char)
        findchr()要在字符串string中查找字符char,找到就返回该值的索引,否则返回-1。
        不能用string.*find()或者string.*index()函数和方法

    (b) 创建另一个叫rfindchr()的函数,查找字符char最后一次出现的位置。
        它跟findchr()工作类似,不过它是从字符串的最后开始向前查找的。

    (c) 创建第三个函数,名字叫 subchr(),声明如下:
        def subchr(string, origchar, newchar)
        subchr()跟 findchr()类似,不同的是,如果找到匹配的字符就用新的字符替换原先字符,返回修改后的字符串。
'''


def findchr(string, char):
    for index, key in enumerate(string):
        if char == key:
            return index
    else:
        return -1


def rfindchr(string, char):
    words = reversed(string)
    for index, key in enumerate(words):
        if char == key:
            return index
    else:
        return -1


def subchr(string, origchar, newchar):
    for index, key in enumerate(string):
        if origchar == key:
            return ''.join([string[:index], newchar, string[index+1:]])
    else:
        return -1
