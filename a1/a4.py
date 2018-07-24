#coding:utf-8

import urllib.parse
a = "中文"
print(parse.quote(a))
b = parse.quote(a)

url = "http://zzk-s.cnblogs.com/s?t=b&w=%s" % b
print(parse.quote(url))