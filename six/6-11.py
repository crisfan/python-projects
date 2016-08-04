# -*- coding:utf-8 -*-

'''
    转换
    (a)创建一个从整数到IP地址的转换程序,如下格式: WWW.XXX.YYY.ZZZ.
    (b)更新你的程序,使之可以逆转换.
'''

# inpr = raw_input('please input some numbers:')

person = ['name', ['saving', 100]]
hubby = person[:]
wifey = list(person)
for i in person:
    print id(i),
print '\n'
for j in hubby:
    print id(j),
print '\n'
for j in wifey:
    print id(j),

person[0] = 'sss'
person[1][1] = 50
print hubby