#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
from Util.handle_json import get_value
from Util.handle_init import handle_ini
proxies={'http':'http://localhost:8888','https':'http://localhost:8888'}
class BaseRequest:
    def send_post(self,url,data,proxies=proxies,cookie=None):
        #发送post请求
        res = requests.post(url=url,data=data,proxies=proxies,cookies=cookie).text
        return res

    def send_get(self,url,data,proxies=proxies,cookie=None):
        #发送get请求
        res = requests.get(url=url,params=data,proxies=proxies,cookies=cookie).text
        return res

    
    def run_main(self,method,url,data,proxies=proxies,cookie=None):
        # 执行方法，传递method、url、data参数
        #return get_value(url)
        base_url = handle_ini.get_value('host')
        if 'http' not in url:
            url = base_url+url
        #print(url)

        if method == 'get':
            res = self.send_get(url,data,proxies,cookie)
        else:
            res =self.send_post(url,data,proxies,cookie)
            try:
                res = json.loads(res)
            except:
                print("这个结果是一个text")
        return res
request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
    request.run_main('get','login',"{'username':'111111'}")






