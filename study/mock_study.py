#coding=utf-8
import mock
import requests
import unittest
url = "http://www.imooc.com/login"
data = {
    "username":"Mushishi",
    "password":"123456"
}
def post_request(url,data):
    res = requests.post(url,data=data).json()
    return res

def get_request(url,data):
    res = requests.get(url,params=data).json()
    return res

print(post_request('http://127.0.0.1:8801/login',data))

class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")

    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username":"111111"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        #res = post_request
        #self.assertEqual("111222",res())

#if __name__ == "__main__":
#    unittest.main()