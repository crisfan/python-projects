# -*- coding:utf-8 -*-

'''
    转换.
    为练习5-13写一个姊妹函数,接受分钟数,返回小时数和分钟数.总时间不变,并且要求小时数尽可能大.
'''

minutes = int(raw_input('please input the minutes:'))
hours = minutes / 60
mins = minutes % 60
print '%d时%d分' % (hours, mins)
