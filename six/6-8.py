# -*- coding:utf-8 -*-

'''
    列表
    给出一个整数值,返回代表该值的英文,比如输入"89"返回"eight-nine"。
    附加题: 能够返回符合英文语法规则的形式,比如输入“89”返回“eighty-nine”。
    本练习中的值限定在0到1,000.
'''

en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num = raw_input('请输入0到1000的数字')
pr = en[int(num[0])]
for i in num[1:]:
    pr += '-' + en[int(i)]
print pr
