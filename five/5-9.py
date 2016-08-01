# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from scrapy.loader.processors import TakeFirst
# test_data = {'project':'guiyang','spider':'gy_nanming'}
# test_data_urlencode = urllib.urlencode(test_data)
# requrl = 'http://192.168.8.111:6800/schedule.json'
# req = urllib2.Request(url=requrl,data=test_data_urlencode)
# req_data = urllib2.urlopen(req)
# res = req_data.read()



a = 'fanyuhao'
re.sub('fanyuhao','chengshufeng',a)
print a

str1 = '\u4f60\u597d'
print str1