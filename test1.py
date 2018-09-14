# coding: utf-8
import requests

url = 'http://prep-yi007.weilian.cn/cps/app/merchant/restRepairListByPage?start=0&length=6'
par = {"mobile": "17607885072",
       "password": "123456"}
data1 = 'account=psg002&enterpriseCode=WEININGSHICHANG&enterpriseId=1473&enterpriseLevel=1&J_S_SESSIONID=1c6a2816-0387-4f6f-8717-83961ac172f6&sessionId=ae8ab5a3bf664a48a19071d96fafa7de'
req = requests.get(url, par)

print req.status_code
print req.text
