#coding = utf-8
import unittest
import HTMLTestRunner
import pprint
from demo1 import RunMain
from mock import mock
from mock_demo import mock_test

class TestMethod(unittest.TestCase):
    def setUp(self):
        url = 'http://coding.imooc.com/api/cate'
        method = "POST"
        self.run = RunMain(url=url,method=method)

    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249192',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': 'jQuery1113042940778651268063_1574172291135',
            'cid': '0',
            'errorCode':1001
        }
        #self.run.run_main = mock.Mock(return_value=data)
        res = mock_test(self.run.run_main,data,url,"POST",data)

        #res = self.run.run_main(url,'POST',data)
        pprint.pprint(res)

        self.assertEqual(res['errorCode'],1001,'测试不通过')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_02'))
    unittest.TextTestRunner().run(suite)