# -*- coding:utf-8 -*-

'''
    循环和数字
    分别使用while和for创建一个循环:
    (a) 写一个while循环,输出整数从0到10。(要确保是从0到10,而不是从0到9或从1到10)
    (b) 做同(a)一样的事,不过这次使用range()内建函数。
'''

# (a)
i = 0
while (i<11):
    print i
    i+= 1

for i in [0,1,2,3,4,5,6,7,8,9,10]:
    print i

# (b)
for i in range(0,11):
    print i
