# -*- coding:utf-8 -*-

'''
    人力资源
    创建一个简单的雇员姓名和编号的程序。
    让用户输入一组雇员姓名和编号。
    你的程序可以提供按照姓名排序输出的功能,雇员姓名显示在前面,后面是对应的雇员编号。
    附加题:添加一项功能,按照雇员编号的顺序输出数据。
'''

myDict = {}
prompt = """
[Q]if you want to quit this order,enter 'q'!
[C]continue,if you want to:!
"""
while True:
    name = raw_input("input employee's name:")
    number = int(raw_input("\ninput employee's number:"))
    if not myDict.get(name):
        myDict[name] = number
    else:
        print 'dict has the same name!'
    choice = raw_input(prompt)
    if choice == 'q':
        break
# 按照姓名排序输出
myList = sorted(myDict.iteritems(), key=lambda x: x[0])
for key, value in myList:
    print "%s:%s" % (key, value)
# 按照编号排序输出
myList = sorted(myDict.iteritems(), key=lambda x: x[1])
for k, v in myList:
    print "%s:%s" % (k, v)
