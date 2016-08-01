# -*- coding:utf-8 -*-

'''
    取余。
    取一个任意小于1美元的金额,然后计算可以换成最少多少枚硬币。
    硬币有1美分,5美分,10美分,25美分四种。1美元等于100美分。
    举例来说,0.76美元换算结果应该是3枚25美分,1枚1美分。
    类似76枚1美分,2枚25美分+2枚10美分+1枚5美分+1枚1美分这样的结果都是不符合要求的。
'''

'''
    思路过于复杂.
'''
x = int(raw_input("请输入你要兑换的金额\n"))
con4=con3=con2=con1=0

if x>=25:
    mod1 = x % 25
    con1 = x /25
    if mod1 >= 10:
        mod2 = mod1 % 10
        con2 = mod1 / 10
        if mod2 >= 5:
            mod3 = mod2 % 5
            con3 = mod2 / 5
            if mod3 >= 1:
                con4 = mod3 / 1
        elif mod2 >= 1:
            con4 = mod2 / 1
    elif mod1 >=5:
        mod2 = mod1 % 5
        con2 = mod1 / 5
        if mod2 >= 1:
            mod3 = mod2 % 1
            con3 = mod2 / 1
    elif mod1 >=1:
        con2 = mod1 / 1
elif x >=10:
    mod1 = x % 10
    con2 = x / 10
    if mod1 >= 5:
        mod2 = mod1 % 5
        con3 = mod1 / 5
        if mod2 >= 1:
            con4 = mod2 / 1
    elif mod1 >= 1:
        con4 = mod1 / 1
elif x >= 5:
    mod1 = x % 5
    con3 = x /5
    if mod1 >= 1:
        con4 = mod1 /1
elif x >= 1:
    con4 = x / 1

print con1,con2,con3,con4
'''
    思路简单
'''
a = int(raw_input('请输入你要兑换的钱币\n'))
N25 = int(a) / 25
N10 = (int(a) - 25 * N25) / 10
N5 = (int(a) - 25 * N25 - 10 * N10) / 5
N1 = int(a) - 25 * N25 - 10 * N10 - 5 * N5
print '%i cents can be changed to:' % int(a)
print '25 Cents: %i' % N25
print '10 Cents: %i' % N10
print ' 5 Cents: %i' % N5
print ' 1 Cents: %i' % N1