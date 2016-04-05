# -*- coding:utf-8 -*-

'''
    循环和运算符
    创建一个包含五个固定数值的列表或元组,输出他们的和。然后修
    改你的代码为接受用户输入数值。分别使用while和for循环实现。
'''

# while
arr = [1,2,3,4,5]
sum, i = 0, 0

while True:
    try:
        sum += arr[i]
        i += 1
    except IndexError:
        break
print 'total is',sum

# for
sum = 0
arr = [1,2,3,4,5]
for i in arr:
    sum += i
print 'total is',sum

# 接受用户输入
sum = 0
while True:
    num = raw_input("please enter number,enter 'q' means exit\n")
    if num.lower() == 'q':
        break
    else:
        sum += int(num)
print 'totle is',sum
