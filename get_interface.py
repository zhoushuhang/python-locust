# coding: utf-8
# coding: utf-8
import requests

# 报修申请数据获取接口
baoxiu_get_url = "http://prep-yi007.weilian.cn/cps/app/merchant/restRepairListByPage?start=0&length=6"

# 报修详情获取接口
baoxiudetail_get_url = "http://prep-yi007.weilian.cn/cps/app/merchant/queryRepairDetail?repairid=1037864731920257024"

# 投诉建议数据获取接口
tousu_get_url = "http://prep-yi007.weilian.cn/cps/app/merchant/restComplaintsListByPage?start=0&length=6"

# 投诉详情获取接口
tousudetail_get_url = "http://prep-yi007.weilian.cn/cps/app/merchant/queryComplaintsDetail?complaintid=369"

# 联系管理员信息获取接口
admin_get_url = "http://prep-yi007.weilian.cn/cps/app/merchant/restProjectContactsListByPage?start=0&length=6"

# 我的商铺信息获取接口
shops_get_url = "http://prep-yi007.weilian.cn/cps/app/shopsRestService/restListByPage?start=0&length=3"

# 合同详情获取接口
contractdetail_get_url = "http://prep-yi007.weilian.cn/cps/app/shopsRestService/querySpConRentcontractById?rentconid=2591"

# 账单缴费数据获取接口
check_get_url = "http://prep-yi007.weilian.cn/cps/app/merchant/restMerchantsettleListByPage?start=0&length=6&gatherflag=1"

# 公告通知获取接口
notice_get_url = "http://prep-yi007.weilian.cn/cps/app/systemBulletinService/restListByPage?start=0&length=8"
