# -*-coding:utf-8 -*-

import datetime
import time
'''
    转换
    (a) 给出两个可识别格式的日期,比如 MM/DD/YY 或者 DD/MM/YY 格式,计算出两个日期间的天数。
    (b) 给出一个人的生日,计算从此人出生到现在的天数,包括所有的闰月。
    (c) 还是上面的例子,计算出到此人下次过生日还有多少天。
'''
# (a)

# 刚开始自己的本办法....
prompt = """
    please input the day like MM/DD/YY:
"""
date = raw_input(prompt).split(' ')
date_one = date[0].split('/')
date_two = date[1].split('/')
i = 0
total = 0
compare = [(int(k), int(v)) for k, v in zip(date_one, date_two)]
for k, v in compare:
    if i == 0:
        total += (k-v) * 365
    elif i == 1:
        total += (k-v) * 30
    else:
        total += k - v
    i += 1
print '两个日期相差', abs(total)

# (b)
prompt = """
    input your birthday:
"""
date = raw_input(prompt).split('/')
date_input = [int(k) for k in date]
date = datetime.date(date_input[0], date_input[1], date_input[2])
print (datetime.date.today() - date).days

# (c)
a = int(time.strftime('%Y', time.localtime()))
days = (datetime.date(a, date_input[1], date_input[2]) - datetime.date.today()).days
days = days if days > 0 else days + 365
print days
