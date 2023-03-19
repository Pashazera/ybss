"""
    Author: Pashazera
    Time  : 2023/3/8 21:00
    File  : catfile.py
    describe :sign_v1.4.jar
"""

import requests
import json
import pandas as pd
import t

# 引入函数库
import datetime as dt
# 获取当前时间
now_time = dt.datetime.now().strftime('%Y%m%d%H%M%S')


serviceId = {"serviceId":"ff8080818315917c018317001d074292"}
ak = {"ak":"9e3d0943d810418fa97a18017caa65d3"}
appId = {"appId":"468DB012B87E4275A1A17A7E184E2A87"}
timestamp = {"timestamp":"20230310161246"}
pageIndex = {"pageIndex":"1"}
pageSize = {"pageSize":"50"}
method = {"method":"POST"}
sign = {"sign":"FDFA84A9F569F79A70A70E9CF7356EDA1ABDF2689808B17A4F945DB2706B2F44"}
url = "http://192.168.242.105:8088/irsp/openApi/ycpfxk/v1"



params = {}
params.update(serviceId)
params.update(ak)
params.update(appId)
params.update(timestamp)
params.update(pageIndex)
params.update(pageSize)
params.update(method)
params.update({"acceptDate":"2019-11"})
params.update(sign)


headers = {
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}

response = requests.post(url=url,headers=headers,params=params)

j = t.getJson(response.json())

print(now_time)
print(response.text)
print(j)
print(pd.DataFrame(j))

