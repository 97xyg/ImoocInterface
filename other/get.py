import requests
import pprint
import json
url = 'http://apitest.zhuliqianbao.com/cloud/user/version/status'
data = {
    'source':'_360',
    'platform':'android',
    'sessionId':'G5xxmt8YGsRMXI8ADmxpt68Kb4TUkJY5SIPXik3Y',
    'appMarket':'_360',
    'channel':'_360',
    'appVersion':'2.7.6',
    'system':'zlqb',
    'client':'1'
}
def send_post(url,data):
    res = requests.get(url=url,data=data)
    return res.json()

pprint.pprint(send_post(url,data),indent=2)
