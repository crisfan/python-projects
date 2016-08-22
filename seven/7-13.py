# -*- coding:utf-8 -*-
import random
'''
    随机数
    修改练习5-17的代码:
    使用random模块中的randint()或randrange()方法生成一个随机数集合:从0到9(包括9)中随机选择,
    生成1到10个随机数,这些数字组成集合A(A可以是可变集合,也可以不是)。
    同理,按此方法生成集合B。每次新生成集合A和B后,显示结果A | B和A & B
'''


# random.randint():用于生成一个指定的范围内的整数(下限必须小于上限)
rand_Aset = set()
for i in range(9):
    rand_Aset.add(random.randint(0, 9))

rand_Bset = set()
for j in range(9):
    rand_Bset.add(random.randint(0, 9))

# 交集,并集
print rand_Aset | rand_Bset
print rand_Aset & rand_Bset
