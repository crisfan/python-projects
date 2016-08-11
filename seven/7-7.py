# -*- coding:utf-8 -*-

'''
    颠倒字典中的键和值。
    用一个字典做输入,输出另一个字典,用前者的键做值,前者的值做键。
'''

# 可以去网上搜索:大神写的代码就是屌炸了天
dict1 = {'fanyuhao': 1993, 'Tom': 1992}
adict = {k: v for v, k in dict1.iteritems()}
print adict
