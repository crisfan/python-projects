# -*- coding:utf-8 -*-

'''
    排序
    (a) 输入一串数字,从大到小排列之.
    (b) 跟a一样,不过要用字典序从大到小排列之.
'''

inp = raw_input('请输入一串数字,并以空格间隔')
num = []
for key in inp.split(' '):
    num.append(key)
num.sort(reverse=True)
print num
print reversed(num)

# 注意两点:序列类型函数sorted()和reversed()
# sorted()返回一个排序后的列表,reversed返回一个可迭代的listreverseiterator对象



