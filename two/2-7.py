# -*- coding:utf-8 -*-

'''
    循环和字串
    从用户那里接受一个字符串输入，然后逐字符显示该字符串。先用while循
    环实现，然后再用for循环实现。
'''

# 字符串有其特有的索引规则:第一个字符的索引是0,最后一个字符的索引是-1。
# while
string = raw_input("please enter a string!\n")
i = 0
x = len(string)
while True:
    if i<x:
        print string[i],
        i+= 1
    else:
        break

# for
string = raw_input('please enter a string!\n')
for x in string:
    print x,
# ','输出的时候空出一格。