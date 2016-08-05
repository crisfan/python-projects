# -*- coding:utf-8 -*-

'''
    字典和列表的方法。
    (a) 创建一个字典,并把这个字典中的键按照字母顺序显示出来。
    (b) 现在根据已按照字母顺序排序好的键,显示出这个字典中的键和值。
    (c) 同(b),但这次是根据已按照字母顺序排序好的字典的值,显示出这个字典中的键和值。
    (注意:对字典和哈希表来说,这样做一般没有什么实际意义,因为大多数访问和排序(如果需要)都是基于字典的键,这里只把它作为一个练习。)
'''

# (a)
dic = {'fan': 1, 'yu': 2, 'hao': 3, 'ys': 2}
keys = sorted(dic.keys())
for key in keys:
    print '%s:%s' % (key, dic[key])
# (b)
for key in sorted(dic, key=lambda x: x[0]):
    print 'key:%s,value:%s' % (key, dic[key])

# (c)
for key in sorted(dic, key=lambda x: (x[0], x[1])):
    print 'key:%s,value:%s' % (key, dic[key])

