# -*- coding:utf-8 -*-

'''
    建立字典。
    给定两个长度相同的列表,比如说,列表[1, 2, 3,...]和['abc', 'def', 'ghi',...],
    用这两个列表里的所有数据组成一个字典,像这样:{1:'abc', 2: 'def', 3: 'ghi',...}
'''

list1 = zip([1, 2, 3], ['abc', 'def', 'ghi'])
dic = dict(list1)
print dic
