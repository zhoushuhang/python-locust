# coding: utf-8
# coding: utf-8
import requests
import json

# 商管平台地址
host = "http://prep-yi007.weilian.cn"


def login(username, pwd):
    url = host + "/cps/app/userCenterRestService/login"

    headers = {
        # "Host": "prep-yi007.weilian.cn",
        # "Connection": "keep-alive",
        # "Content-Length": "70",
        # "Accept": "application/json, text/plain, */*",
        # "Origin": "http://prep-yi007.weilian.cn",
        # # "sessionId": "4445a0ac1a9d447cb916aef01610ecca",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Content-Type": "application/json",
        # "Referer": "http://prep-yi007.weilian.cn/cps/app/static/index.html",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Cookie": "account = psg002; enterpriseCode=WEININGSHICHANG; enterpriseId=1473; enterpriseLevel=1; J_S_SESSIONID=1c6a2816-0387-4f6f-8717-83961ac172f6; sessionId=083bb954b1c741ba84dfd4cbe74ab92d"
    }

    body = {
        "mobile": username,
        "password": pwd,
            }
    # body_json = json.dumps(body)

    # s = requests.session()   # 不要写死session

    # r1 = requests.post(url, json=body_json, headers=headers)
    r1 = requests.post(url, body, headers)
    return r1.content  # python2的return这个
    # return r1.content.decode("utf-8")  # python3


def is_login_sucess(res):
    if u"用户名或密码错误" in res:
        return False
    elif "1473" in res:
        return True
    else:
        return False


if __name__ == "__main__":
    # s = requests.session()
    a = login("17607885072", "123456")
    result = is_login_sucess(a)
    print(u"测试结果：%s" % result)
    print a
