import requests
import pprint

url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
data = {
    'cart':'11'
}

def send_post(url,data):
    res = requests.post(url=url,data=data)
    return res.json()

pprint.pprint(send_post(url,data))