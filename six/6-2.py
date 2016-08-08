# -*- coding:utf-8 -*-
import string
import keyword
'''
    字符串标识符
    修改例6-1的idcheck.py脚本,使之可以检测长度为一的标识符,并且可以识别Python关键字。
    对后一个要求,你可以使用keyword模块(特别是 keyword.kwlist)来帮你。
'''

words = raw_input('请输入标识符:')
length = len(words)
first = words[0]
last = words[1:]
alphas = string.letters + '_'
all = alphas + string.digits
keywords = keyword.kwlist

if length > 1:
    if first in alphas:
        for key in last:
            if key not in all:
                print u'不能做为标识符'
                break
        else:
            if words not in keywords:
                print u'可以做为标识符'
            else:
                print u'不能占用关键字'
    else:
        print u'首字符必须是字母或者下划线'
elif length == 1:
    if first in string.letters:
        print u'可以做为标识符'
    elif first == '_':
        print u'单独的下划线不能做为标识符'
    else:
        print u'单独字母时,首字母必须是字母'


'''
    注意程序里面for循环的用法
'''