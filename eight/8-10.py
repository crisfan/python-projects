# -*- coding:utf-8 -*-

'''
    文本处理.
    统计一句话中的元音, 辅音以及单词(以空格分割)的个数.
    忽略元音和辅音的特殊情况, 如 "h", "y", "qu" 等.
    附加题: 编写处理这些特殊情况的代码.
'''

vowel = ['a', 'i', 'e', 'o', 'u']
def count(sentence):
    vo_sum = 0
    num_sum = 0
    blank_sum = 1
    for word in sentence:
        num_sum += 1
        if word in vowel:
            vo_sum += 1
        elif word == ' ':
            blank_sum += 1
    return vo_sum, num_sum-vo_sum-blank_sum+1, blank_sum

print count('I am a good boy')