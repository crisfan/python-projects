# -*- coding:utf-8 -*-

'''
    矩阵
    处理矩阵M和N的加和乘操作。
'''
# 加操作
m = [1, 2, 3, 4, 5, 6]
n = [1, 2, 3, 4, 5, 6]
length = len(m)
mix = []
for index in range(length):
    sum = m[index] + n[index]
    mix.append(sum)
for index in range(length):
    if index < 3:
        print mix[index],
    elif index == 3:
        print
        print mix[index],
    else:
        print mix[index],
