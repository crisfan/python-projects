# -*- coding:utf-8 -*-

' 3-12.py -- choose to built or read text file'

import os

'''
	合并源文件。
	将两段程序合并成一个,给它起一个你喜欢的名字,
	比方 readNwriteTextFiles.py。让用户自己选择是创建还是显示一个文本文件。
'''
ls = os.linesep
x = raw_input('1.建立文件 2.显示文本\n')
if x == '2':
    fname = raw_input('Enter filename: ')
    try:
    	fobj = open(fname, 'r')
    except IOError, e:      # 这里可以直接用os.path.exist()函数
    	print '***file open error', e
    else:
		for eachLine in fobj:
			print eachLine.strip('\n')  # strip():移除字符串的头尾指定的字符
    fobj.close()
elif x == '1':
 	while True:
 		fname = raw_input("please enter the filename:")
 		if os.path.exists(fname):
 			print "error:'%s' already exists" % fname
 		else:
 			break
 	all = []
 	print "\nenter lines('.' by itself to quit)\n"

	# loop util user terminates input
	while True:
		entry = raw_input(">")
		if entry == ".":
			break
		else:
			all.append(entry)
	# write lines to file with proper line-ending
	fobj = open(fname, "w")
	# writelines的参数是序列，可以将序列中的元素迭代写入文件。
	fobj.writelines(["%s%s" % (x, ls) for x in all])
	fobj.close()
	print "DONE!"


 
