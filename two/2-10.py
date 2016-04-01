# -*- coding:utf-8 -*-

'''
    带循环和条件判断的用户输入
    使用raw_input()函数来提示用户输入一个1和100之间的数,如果用户输入的数满足这个条件,
    显示成功并退出。否则显示一个错误信息然后再次提示用户输入数值，直到满足条件为止。
'''

# 这个功能倒是齐全,但是代码看着就是不舒服，有好的可以分享。
while True:
    num = raw_input('请输入1-100之间的数\n')
    if num.isdigit():
        if int(num)>=1 and int(num)<=100:
            print 'successful!'
            break


