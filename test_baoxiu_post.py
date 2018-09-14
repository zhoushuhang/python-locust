# coding: utf-8
# coding: utf-8
import json
import requests
body = {"repairtype": 1, "repairman": "周大福",
        "repairmantel": "13802738933", "projectid": "107",
        "projectname": "水街市场", "repairaddress": "水街市场水产批发",
        "repairreason": "水管漏水2",
        "repairPicList": [{"name": "2.png", "size": 32446,
                           "pictureurl": "https://files.scn.weilian.cn/d/f549303366d39a534a100c065bfa189a"}]}
# json串数据使用
body1 = json.dumps(body)
# 普通数据使用
# textmod = parse.urlencode(textmod).encode(encoding='utf-8')
print(body1.encode(encoding='utf-8'))
# result = json.dumps(body1, encoding='UTF-8', ensure_ascii=False)  # 使用json进行格式转换，使输出显示为中文
# print result
# 输出内容:b'{"params": {"user": "admin", "password": "zabbix"}, "auth": null, "method": "user.login", "jsonrpc": "2.0", "id": 1}'
header_dict = {"sessionId": "c95e83651a0444bdb20a5c6b95c09198", "Content-Type": "application/json"}
url = 'http://prep-yi007.weilian.cn/cps/app/merchant/submitMyRepair'
req = requests.post(url=url, data=body1, headers=header_dict)
# res = requests.urlopen(req)
# res = res.read()
print req
print req.content
