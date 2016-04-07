# -*- coding:utf-8 -*-

'''
	标识符。
	下面哪些是Python合法的标识符？如果不是，请说明理由。在合法的标识符中，哪些是关键字？
	int32  40XL  $aving$  printf  print
	_print  this  self  __name__ 0X40L
	bool  true  big-daddy 2hot2touch type
	thisIsn'tAVar thisIsAVar R_U_Ready Int  True
	if  do  counter-1 access  -
'''

# 合法标识符：以字母或下划线开头,剩下的字符字母，下划线，数字。

# 合法表示符：int32 printf print _print this self __name__
# 		   bool true type thisIsAVar 
# 		   R_U_Ready Int True if do  access 
# 关键字：print if   (可以通过iskeyword()函数查看)