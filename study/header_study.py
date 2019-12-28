#coding=utf-8
import requests
import pprint
import json
header = {
    'Host':'m.imooc.com',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://m.imooc.com/',
    'Accept-Language':'zh-CN,zh;q=0.9'
}

proxies = {'http':'http://localhost:8888','https':'http://localhost:8888'}
res = requests.get("https://m.imooc.com/api/search/searchword",headers = header,proxies=proxies,verify=False).json()
pprint.pprint(res)