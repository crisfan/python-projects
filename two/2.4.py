# -*- coding:utf-8 -*-

'''
    使用raw_input()函数得到用户输入
    (a) 创建一段脚本使用 raw_input() 内建函数从用户输入得到一个字符串，然后显示这个用户刚刚键入的字符串。
    (b) 添加一段类似的代码，不过这次输入的是数值。将输入数据转换为一个数值对象，（使用int()或其它数值转换函数）
        并将这个值显示给用户看。（注意，如果你用的是早于1.5的版本，你需要使用string.ato*() 函数执行这种转换）
'''

# (a)
input = raw_input("please input something you like!\n")
print input # ForkEyes

# (b)
input = raw_input("please input number!\n")
a = int(input)
print type(a),a # <type 'int'> 8