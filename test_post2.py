# coding: utf-8
# coding: utf-8
import requests
import json
import re


def session():
    url = 'http://prep-yi007.weilian.cn/cps/app/userCenterRestService/login'

    headers_dict = {"Content-Type": "application/json"}

    body1 = {"mobile": "17607885072", "password": "123456"}

    body1 = json.dumps(body1)
    s = requests.session()
    r1 = s.post(url=url, data=body1, headers=headers_dict)
    print r1.json()
    r2 = str(r1.json())
    print r2
    positionComPile = re.compile("'sessionId':.*?,", re.S)
    position = re.findall(positionComPile, r2)
    print(position)
    for i in position:

        print(i.split(':')[1].replace(",","").split("'")[1])
        sessionno = (i.split(':')[1].replace(",","").split("'")[1])
        return sessionno


# searchObj = re.search(r"\'sessionId\'\\:\s[0-9a-zA-Z]\'\\,$", r2)
# print searchObj.group()
# print r1.json()
# print r1.headers
# print r1.cookies
# print r1.text
# print r1.content
# print r1.status_code

def get(s, session):
    # 报修申请数据获取接口
    headers_dict = {"sessionId": session, "Content-Type": "application/json"}
    baoxiu_get_url = "http://prep-yi007.weilian.cn/cps/app/merchant/restRepairListByPage?start=0&length=6"

    req = s.get(url=baoxiu_get_url, headers=headers_dict)
    return req


if __name__ == "__main__":
    s = requests.session()
    session = session()
    print session
    a = get(s, session)
    print a.content
    print a.status_code
# print("测试结果：%s"%result)
# print req
# print req.content
