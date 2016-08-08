# -*- coding:utf-8 -*-

'''
    算术
    更新上一章里面你的得分测试练习方案,把测试得分放到一个列表中去。
    你的代码应该可以计算出一个平均分,见练习2-9和练习5-3。
'''

scoreList = []
while True:
    inp = raw_input("Please input scores:... ")
    if inp != 'a':
        score = float(inp)
        scoreList.append(score)
    else:
        break
i = 0
for k in scoreList:
    i = i + k
print 'The average is %4.2f' % (i / len(scoreList))
