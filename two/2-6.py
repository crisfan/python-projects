# -*- coding:utf-8 -*-

'''
    条件判断
    判断一个数是正数，还是负数或者等于0. 开始先用固定的数值，然
    后修改你的代码支持用户输入数值再进行判断。
'''

# x = 9

while True:
    x = raw_input("请输入一个数字,输入q退出!\n")
    if x.lower() == 'q':
        break
    else:
        if int(x)<0:
            print "x是负数哦！"
        elif int(x)>0:
            print "x是正数哦！"
        else:
            print "x是零哦！"

# raw_input():把所有输入都当做字符串处理，所以需要在比较时用Int()转化。


