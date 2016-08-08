# -*- coding:utf-8 -*-

'''
    字符串
    string模块中是否有一种字符串方法或者函数可以帮我鉴定一个字符串。
    是否是另一个大字符串的一部分?
'''

# 成员操作符 in
a = 'ab'
b = 'vghgab'
if a in b:
    print 'a in b'
else:
    print 'a is not in b'

