#coding = utf-8
import unittest
import HTMLTestRunner
from demo1 import RunMain

class TestMethod(unittest.TestCase):
    def setUp(self):
        url = 'http://coding.imooc.com/api/cate'
        method = "POST"
        self.run = RunMain(url=url,method=method)
    def test_03(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
                'timestamp': '1507034803124',
                'uid': '5249191',
                'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
                'secrect': '078474b41dd37ddd5efeb04aa591ec12',
                'token': 'jQuery1113042940778651268063_1574172291135',
                'cid': '0'
        }
        res = self.run.run_main(url,'POST',data)
        print('这是第1个case')

        self.assertEqual(res['errorCode'],1000,'测试通过')

    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249192',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': 'jQuery1113042940778651268063_1574172291135',
            'cid': '0'
        }

        res = self.run.run_main(url,'POST',data)
        print('这是第2个case')

        self.assertEqual(res['errorCode'],1007,'测试不通过')


if __name__ == '__main__':
    filepath = "../report/HtmlReport.html"
    fp = open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_03'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="This is first report")
    runner.run(suite)
    fp.close()