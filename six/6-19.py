# -*- coding:utf-8 -*-

'''
    多列输出
    有任意项的序列或者其他容器,把它们等距离分列显示.
    由调用者提供数据和输出格式.
    例如,如果你传入100个项并定义3列输出,按照需要的模式显示这些数据.
    这种情况下,应该是两列显示33个项,最后一列显示4个.
    你可以让用户来选择水平排序或者垂直排序.
'''

# 水平排序
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
length = len(alist)
Input = raw_input('please input row that you want:')
# 每一列多少个数
column_num = length / int(Input)
for index, data in enumerate(alist):
    if (index+1) % int(Input) != 0:
        print data,
    else:
        print data,
        print

print '\naaaaa\n'

# 垂直排序
flag = 0
column = int(Input)
# 这里其实有修改的空间
for index in range(length):
    # 判断是否需要空字符填充
    if index < column_num:
        i = 0
        # 不需要用空字符填充时,循环输出每一行
        while i < column:
            print alist[index],
            # 存放每一列最后一个元素的index
            flag = index
            index += column_num
            i += 1
        else:
            # 下一行
            print
    else:
        # 当下标在前面出现过,则用空白字符代替
        while index < flag+1:
            print ' ',
            index += column_num
        if index < length:
            flag = index
            print alist[index],
            print
        else:
            break
