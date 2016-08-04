# -*- coding:utf-8 -*-

'''
    字符串.
    写一个函数,返回一个跟输入字符串相似的字符串,要求字符串的大小写反转.
    比如,输入"Mr.Ed",应该返回"mR.eD"作为输出.
'''


def change(str1):
    str2 = ''
    for i in str1:
        if i == i.upper():
            str2 += i.lower()
        else:
            str2 += i.upper()
    return str2
inpr = raw_input('please input a string:')
print change(inpr)
