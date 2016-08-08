# -*-coding:utf-8 -*-
import random

'''
    随机数
    设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,下面是规则。
    你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从下面的规则中产生,
    这个规则本身是个悖论。
    (a)布包石头.
    (b)石头砸剪子,
    (c)剪子剪破布.
    在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,然后由你的程序来决定一个胜利者或者平手。
    注意:最好的算法是尽量少的使用if语句。
'''

prompt = """
    (S)Tone
    (H)ears
    (C)Loth
"""
user_choice = raw_input(prompt)
# 计算机随机产生一个选择
computer_choice = random.choice('SHC')
# 定义一个字典存放所有结果
adict = {'equal': {'SS', 'HH', 'CC'}, 'user win': {'SH', 'HC', 'CS'}, 'computer win': {'SC', 'HS', 'CH'}}
results = user_choice + computer_choice
for key,value in adict.iteritems():
    if results not in value:
        continue
    else:
        print key
        break

