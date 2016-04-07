#!/usr/bin/env python

"makeTextFile.py -- create text file"

import os

ls = os.linesep

#get filename
while True:
    fname = raw_input("please enter the filename:")
    if os.path.exists(fname):
        print "error:'%s' already exists" % fname
    else:
        break

#get file content lines
all = []
print "\nenter lines('.' by itself to quit)\n"

#loop util user terminates input
while True:
    entry = raw_input(">")
    if entry == ".":
        break
    else:
        all.append(entry)
#write lines to file with proper line-ending
fobj = open(fname, "w")
# writelines的参数是序列，可以将序列中的元素迭代写入文件。
fobj.writelines(["%s%s" % (x, ls) for x in all])
fobj.close()
print "DONE!"