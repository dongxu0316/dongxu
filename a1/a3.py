#coding:utf-8
import requests

from urllib import parse


url = "http://zzk-s.cnblogs.com/s?t=b&w=%E4%B8%AD%E6%96%87"

r = requests.get(url)
#返回的url
print(r.url)


res = r.url
#
print(parse.unquote(res))


res1 = res.split("?")[1]
res2 = res1.split("&")
print(res2)
for i in res2:
    if "w" in i:
        print(i.split("=")[1])

b = "%E4%B8%AD%E6%96%87"
c = parse.unquote(b)
print(c)