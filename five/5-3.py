# -*- coding:utf-8 -*-

'''
    标准类型操作符。
    写一段脚本，输入一个测验成绩，根据下面的标准，输出他的评分成绩（A-F）。
    A:90~100 B:80~89 C:70~79 D:60~69 F:<60
'''

x = float(raw_input('输入你的成绩\n'))
if x>=90:
    print 'A'
elif x>=80:
    print 'B'
elif x>=70:
    print 'C'
elif x>=60:
    print 'D'
elif x<60:
    print 'F'
