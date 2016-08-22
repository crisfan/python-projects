# -*- coding:utf-8 -*-

import random

'''
    用户验证
    修改前面的练习,要求用户输入A | B和A & B的结果,并告诉用户他(或她)的答案是否正确,
    而不是将A | B和A & B的结果直接显示出来。
    如果用户回答错误,允许他(或她)修改解决方案,
    然后重新验证用户输入的答案。如果用户三次交的答案均不正确,程序将显示正确结果。
    附加题:运用你关于集合的知识,创建某个集合的潜在子集,并询问用户此潜在子集是否真是该集合的子集,
    要求和主程序一样有显示更正和答案的功能。
'''

rand_Aset = set()
for i in range(9):
    rand_Aset.add(random.randint(0, 9))

rand_Bset = set()
for j in range(9):
    rand_Bset.add(random.randint(0, 9))

# 交集,并集
rand_set1 = rand_Aset | rand_Bset
rand_set2 = rand_Aset & rand_Bset
x = 0
while x <= 2:
    iu = raw_input('please input A | B :')
    iu = set(iu)
    if iu == rand_set1:
        break
    x += 1
else:
    print 'this is a true answer', rand_set1


