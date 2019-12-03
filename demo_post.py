import requests
import pprint

url = 'http://coding.imooc.com/api/cate'
data = {'timestamp':'1507034803124',
        'uid':' 5249191',
        'uuid':' 5ae7d1a22c82fb89c78f603420870ad7',
        'secrect':' 078474b41dd37ddd5efeb04aa591ec12',
        'token':' 7d6f14f21ec96d755de41e6c076758dd',
        'cid':' 0'

}

def send_post(url,data):
    res = requests.post(url=url,data=data)
    return res.json()

pprint.pprint(send_post(url,data))