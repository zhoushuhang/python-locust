# coding: utf-8
# coding: utf-8
import json
import requests

# 登录接口
login_url = "http://prep-yi007.weilian.cn/cps/app/userCenterRestService/login"
login_body = {"mobile": "17607885072", "password": "e10adc3949ba59abbe56e057f20f883e"}

# 退出登录接口
logout_url = "http://prep-yi007.weilian.cn/cps/app/userCenterRestService/logout"
logout_body = {"data": [null], "returnCode": 1, "msg": null, "html":null}

# 报修申请新增post接口
baoxiu_url = "http://prep-yi007.weilian.cn/cps/app/merchant/submitMyRepair"
baoxiu_body = {"repairtype": 1, "repairman": "周大福",
               "repairmantel": "13802738933", "projectid": "107",
               "projectname": "水街市场", "repairaddress": "水街市场水产批发",
               "repairreason": "水管漏水2",
               "repairPicList": [{"name": "2.png",
                                  "size": 32446,
                                  "pictureurl": "https://files.scn.weilian.cn/d/f549303366d39a534a100c065bfa189a"}]}

# 投诉建议新增post接口
tousu_url = "http://prep-yi007.weilian.cn/cps/app/merchant/submitMyComplaints"
tousu_body = {{"complainttype": "0", "object": "水街市场空调不制冷",
               "projectid": "107", "projectname": "水街市场", "content": "水街市场空调不制冷",
               "complaintman": "周大福", "telephone": "13802738933", "address": "水街市场空调不制冷",
               "complaintPicList": [{"name": "1.png", "size": 24187,
                                     "pictureurl": "https://files.scn.weilian.cn/d/53ecc31e8e329e00df6438db4f648ffb"},
                                    {"name": "2.png", "size": 32446,
                                     "pictureurl": "https://files.scn.weilian.cn/d/f549303366d39a534a100c065bfa189a"},
                                    {"name": "3.png", "size": 15770,
                                     "pictureurl": "https://files.scn.weilian.cn/d/256010e2f36e32ca05534d054f37e278"}]}}

# 修改登录密码post接口
passwordchange_url = "http://prep-yi007.weilian.cn/cps/app/userCenterRestService/changePassword"
passwordchange_body = {"oldPassword": "123456", "password": "1234567"}

# 修改头像post接口
touxiang_url = "http://prep-yi007.weilian.cn/cps/app/merchant/updateMerchantHeader"
touxiang_body = {"headpicaddress": "https://files.scn.weilian.cn/d/f549303366d39a534a100c065bfa189a"}
