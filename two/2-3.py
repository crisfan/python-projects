# -*- coding:utf-8 -*-

'''
    数值和运算符
    启动交互解释器，使用Python对两个数值(任意类型）进行加、减、乘、除运算。
    然后使用取余运算符来得到两个数相除的余数，最后使用乘方运算符求A数的B次方。
'''

# 加、减、乘、除
# python支持五种基本的数字类型:有符号整数(int),长整数(long),布尔值(bool),浮点值(float),复数(complex)
x = 5
y = 6
w = 10.5
z = x + y
print z # 11
z = y - x
print z # 1
z = x * y
print z # 30
z = y / x
print z # 1
z = x + w
print z # 15.5

# 取余运算
x = 8
y = 10
z = y % x
w = x % y
print z # 2
print w # 8

# 乘方运算
z = y ** x
print z # 100000000
