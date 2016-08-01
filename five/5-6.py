# -*- coding:utf-8 -*-

'''
    算术。
    写一个计算器程序你的代码可以接受这样的表达式,两个操作数加一个运算符:N1 运算符 N2.
    其中 N1 和 N2 为整数或浮点数,运算符可以是+, -, *, /, %, ** 分别表示加法,减法,乘法,整数除,取余和幂运算。
    计算这个表达式的结果,然后显示出来。提示: 可以使用字符串方法split(),但不可以使用内建函数eval().
'''
# str.split(str="", num=string.count(str)).
x = raw_input('请输入你要计算的表达式\n')
a = int(x.split()[0])
b = int(x.split()[2])
if '+' == x.split()[1]:
    print a + b
elif '-' == x.split()[1]:
    print a - b
elif '*' == x.split()[1]:
    print a * b
elif '/' == x.split()[1]:
    print a / b
elif '%' == x.split()[1]:
    print a % b
elif '**' == x.split()[1]:
    print a ** b
