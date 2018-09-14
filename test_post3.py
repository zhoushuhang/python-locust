# from urllib import parse,request
# coding: utf-8
# coding: utf-8
import json
import requests
textmod = {"mobile": "17607885072", "password": "123456"}
# json串数据使用
textmod = json.dumps(textmod)
print textmod
# 普通数据使用
# textmod = parse.urlencode(textmod).encode(encoding='utf-8')
print(textmod)
# 输出内容:b'{"params": {"user": "admin", "password": "zabbix"}, "auth": null, "method": "user.login", "jsonrpc": "2.0", "id": 1}'
header_dict = {"Content-Type": "application/json"}
url = 'http://prep-yi007.weilian.cn/cps/app/userCenterRestService/login'
req = requests.post(url=url, data=textmod, headers=header_dict)
# res = requests.urlopen(req)
# res = res.read()
print(req)
print req.content
# 输出内容:b'{"jsonrpc":"2.0","result":"37d991fd583e91a0cfae6142d8d59d7e","id":1}'
# print(res.decode(encoding='utf-8'))
# 输出内容:{"jsonrpc":"2.
