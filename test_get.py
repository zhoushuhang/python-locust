# coding: utf-8
# coding: utf-8
import requests

url = "http://prep-yi007.weilian.cn/cps/app/merchant/restRepairListByPage?start=0&length=6"

head = {"sessionId": "50311d0d402546a998c2b6a5c91326a3"}

req = requests.get(url=url, headers=head)
print(req)
print req.content
