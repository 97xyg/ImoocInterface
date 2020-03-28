#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
from Util.handle_init import handle_ini

class BaseRequest:
    def send_post(self,url,data):
        #发送post请求
        res = requests.post(url=url,data=data).text
        return res

    def send_get(self,url,data):
        #发送get请求
        res = requests.get(url=url,params=data).text
        return res

    # 执行方法，传递method、url、data参数
    def run_main(self,method,url,data):
        base_url = handle_ini.get_value('host')
        if 'http' in base_url:
            url = base_url+url
        print(url)
        print('**********')
        if method == 'get':
            res = self.send_get(url,data)
        else:
            res =self.send_post(url,data)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res

if __name__ == "__main__":
    request = BaseRequest()
    request.run_main('post','login',"{'username':'111111'}")







