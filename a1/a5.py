#coding:utf-8

import  requests

s = requests.session()

print(s.headers)


{'Connection': 'keep-alive', 'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*'}