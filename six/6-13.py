# -*- coding:utf-8 -*-

'''
    字符串.
    string模块包含三个函数,atoi(),atol(),和atof(),
    它们分别负责把字符串转换成整数,长整型,和浮点型数字.
    从Python1.5起,Python的内建函数int(),long(),float()也可以做相同的事了,complex()函数可以把字符串转换成复数.
    (然而1,5之前,这些转换函数只能工作于数字之上)
'''


def atoc(inputs):
    print complex(inputs).real
    print complex(inputs).imag

inputs = raw_input('please input a complex number ... ')
atoc(inputs)