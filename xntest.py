# coding: utf-8
import json
from locust import HttpLocust
from locust import TaskSet
from locust import task


class TestDemo(TaskSet):
    '''用户行为：商管APP登录'''
    @task(1)
    def login_app(self):
        # 定义requests的请求头
        header = {"Content-Type": "application/json"}
        body1 = {"mobile": "17607885072", "password": "123456"}

        body1 = json.dumps(body1)
        r1 = self.client.post("/cps/app/userCenterRestService/login", data=body1, headers=header)
        print(r1.status_code)
        assert r1.status_code == 200


class websitUser(HttpLocust):
    task_set = TestDemo
    min_wait = 3000
    max_wait = 6000


if __name__ == "__main__":
    import os
    os.system("locust -f xntest.py --host=http://prep-yi007.weilian.cn")