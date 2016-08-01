# -*- coding:utf-8 -*-

'''
    取余。
    判断给定年份是否是闰年.
    使用下面的公式:
    一个闰年就是指它可以被4整除,但不能被100整除,或者它既可以被4又可以被100整除.
    比如1992,1996和2000年是闰年,但1967和1900则不是闰年.下一个是闰年的整世纪是2400年。
'''
def LeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return True
    else:
        return False

year = int(raw_input('请输入年份\n'))
if LeapYear(year):
    print '%d年是闰年' % year
else:
    print '%d年不是闰年' % year

