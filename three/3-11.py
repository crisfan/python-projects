# -*- coding:-utf-8 -*-
#!/usr/bin/env Python

'''
	字符串格式化不再抑制readTextFile.py中print语句生成的NEWLINE字符,修改你的代码,
	在显示一行之前删除每行末尾的空白。这样,你就可以移除print语句末尾的逗号了。 
	提示:使用字符串对象的strip()方法
'''

'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter filename: ')


# attempt to open file for reading

try:
	fobj = open(fname,'r')
except IOError,e:      # 这里可以直接用os.path.exist()函数
	print '***file open error',e
else:
	# display contents to the screen
	for eachLine in fobj:
		print eachLine.strip('\n') # strip():移除字符串的头尾指定的字符
	fobj.close()