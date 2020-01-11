import requests
import json
url = 'http://apitest.zhuliqianbao.com/cloud/user/account/deviceinfo?platform=android&sessionId=_DHpATswwFXA726l5tBdGbWFEgNSz_fQmer5zvX8&appMarket=_360&channel=_360&appVersion=2.7.6&system=zlqb&client=1'
data = {
    'androidId':'db873ac677a7fe27',
    'osApiVersion':'23',
    'deviceIMEI':'864083031948954',
    'macAddress':'ec:01:ee:73:25:ae',
    'deviceType':'OPPO OPPO R9s',
    'deviceModel':'OPPO OPPO R9s',
    'deviceOS':'6.0.1',
    'lat':'0.0',
    'lng':'0.0'
}
def send_post(url,data):
    res = requests.post(url=url,data=data)
    return res.json()

print(send_post(url,data))