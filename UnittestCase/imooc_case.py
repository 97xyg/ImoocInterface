#coding=utf-8
import requests
import sys
import os
base_path = os.getcwd()
print(base_path)
sys.path.append(base_path)
import unittest
import json
import mock
from Base.base_request import request
def read_json():
    with open(base_path+"/Config/user_data.json") as f:
        data = json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]

host = 'http://www.imooc.com/'
class ImoocCase(unittest.TestCase):
    def test_banner(self):
        url = host+'api3/getbanneradvertver2'
        data = {
            'timestamp': '1561269343481',
            'uid': '7213561',
            'token': 'a14667648b0a88f54900a1360dce9436',
            'type': '1',
            'marking': 'androidbanner',
            'uuid': '41b650ef846688193728ff7381eb6c1c',
            'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI4MjI3OTI4IiwianRpIjoiMGQ5YmEzOWQzOGIwYTU3ZWY4MTg1M2QxM2ZmMGVmM2YiLCJkZXZpY2UiOiJtb2JpbGUifQ.SIhwi9_6AkP4gx3SQULZYsD8OstVk55d6w3gTA0RvkE'
        }
        mock_method = mock.Mock(return_value=get_value('api3/getbanneradvertver2'))
        request.run_main = mock_method
        res = request.run_main('post',url,data)
        print(res)
        self.assertEqual(res['errorCode'],1000)

if __name__ =="__main__":
    unittest.main()
