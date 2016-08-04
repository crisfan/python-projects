# -*- coding:utf-8 -*-

'''
    字符串
    (a)更新你在练习2-7里面的方案,使之可以每次向前向后都显示一个字符串的一个字符.
    (b)通过扫描来判断两个字符串是否匹配(不能使用比较操作符或者cmp()内建函数)。
    附加题:在你的方案里加入大小写区分.
    (c)判断一个字符串是否重现(后面跟前面的一致).
    附加题:在处理除了严格的回文之外,加入对例如控制符号和空格的支持。
    (d)接受一个字符,在其后面加一个反向的拷贝,构成一个回文字符串.
'''
# (a)
inp = raw_input('请输入一段字符串')
length = len(inp) - 1
for key in inp:
    num = inp.index(key)
    if num == 0:
        print '%s字符为首字符' % key
        print '%s后面的字符为%s' % (key, inp[num+1])
    elif num == length:
        print '%s字符为尾字符' % key
        print '%s字符前面的字符为%s' % (key, inp[num-1])
    else:
        print '%s前面的字符为%s,后面的字符为%s' % (key, inp[num-1], inp[num+1])

# (b)
a = raw_input('输入a变量值')
b = raw_input('输入b变量值')
a_len = len(a)
b_len = len(b)

if a_len == b_len:
    for index in range(a_len):
        if a[index] != b[index]:
            print '两个字符不匹配'
            break
    else:
        print '两个字符匹配'
else:
    print '两个字符串不匹配'

# (c)
c = raw_input('请输入一段字符串')
c_len = len(c)
mid = c_len / 2
for index in range(mid):
    last = -(index + 1)
    if cmp(c[index], c[last]):
        print '此字符串不是回文字符串'
        break
else:
    print '此字符串是回文字符串'

# (d)
d = raw_input('请输入一段字符串')
print d + d[::-1]
