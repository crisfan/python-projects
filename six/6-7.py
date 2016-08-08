# -*- coding:utf-8 -*-

'''
    调试
    看一下在例6.5中给出的代码(buggy.py)
    (a) 研究这段代码并叙述这段代码想做什么,在所有的(#)处都要填写你的注释。
    (b) 这个程序有一个很大的问题,比如输入6,12,20,30,等它会死掉,实际上它不能处理任何的偶数,找出原因。
    (c) 修正(b)中提出的问题。
'''

# 目的是：输入一个自然数，按照这个数创建一个增序的列表，
# 逐个检查该自然数是否能被列表中元素整除。如果能，就从列表中删除该列表元素
num_str = raw_input('Enter a number: ')
# 字符串整形化
num_num = int(num_str)
fac_list = range(1, num_num+1)
print "BEFORE:", fac_list
i = 0
# 删除列表中能整除num_num的元素
while i < len(fac_list):
    if num_num % fac_list[i] == 0:
        del fac_list[i]
    else:
        i += 1
print "AFTER", fac_list
