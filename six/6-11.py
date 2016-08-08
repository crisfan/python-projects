# -*- coding:utf-8 -*-

'''
    转换
    (a) 创建一个从整数到IP地址的转换程序,如下格式: WWW.XXX.YYY.ZZZ。
    (b) 更新你的程序,使之可以逆转换。
'''

inpr = int(raw_input('please input the number that you want to translate:'))
decimal_4 = inpr % 255
integer = inpr / 255

if integer > 255*255:
    integer_1 = integer / 255*255
    decimal_2 = integer % 255*255
elif integer > 255:
    integer_2 = integer / 255
    decimal_3 = integer % 255
    print '0.'+str(integer_2)+'.'+str(decimal_3)+'.'+str(decimal_4)
else:
    integer_3 = integer
    print '0.'+'0.'+str(integer_3)+'.'+str(decimal_4)


