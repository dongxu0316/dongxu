# coding:utf-8

import json

d = {
    "a": None,
    "b": 123,
    "c": "111",
    "d":True,
    "e": ["a","b"],
    "f":12.3,
    "g":False

}
print(type(d))
print(d)
#字典转josn
d_json = json.dumps(d)
print(type(d_json))
print(d_json)
#json转dict
j_dict = json.loads(d_json)
print(type(j_dict))
print(j_dict)