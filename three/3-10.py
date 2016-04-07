#!/usr/bin/env Python

'''
	异常。
	使用类似readTextFile.py中异常处理的方法取代makeTextFile.py中对os.path.exists()的调用。
	反过来, 用os.path.exists()取代readTextFile.py中的异常处理方法。
'''

'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter filename: ')
print

# attempt to open file for reading
# try-except-else 结构
try:
	fobj = open(fname,'r')
except IOError,e:      # 这里可以直接用os.path.exist()函数
	print '***file open error',e
else:
	# display contents to the screen
	for eachLine in fobj:
		print eachLine, # 注意这里用逗号的理解。
	fobj.close()
