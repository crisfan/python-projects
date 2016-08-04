# -*- coding:utf-8 -*-

'''
    字符串.创建一个string.strip()的替代函数:接受一个字符串,去掉它前面和后面的空格
    (如果使用 string.*strip()函数那本练习就没有意义了)
'''

inp = raw_input('请输入一段字符串')
# 删除后面的空格
while True:
    if inp[-1] == ' ':
        inp = inp[:-1]
    else:
        break
# 删除前面的空格
while True:
    if inp[0] == ' ':
        inp = inp[1:]
    else:
        break
print inp
