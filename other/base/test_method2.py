#coding = utf-8
import unittest
import HTMLTestRunner
from other.demo1 import RunMain

class TestMethod(unittest.TestCase):
    def setUp(self):
        url = 'https://www.imooc.com/course/ajaxcoursenewrecom'
        method = "GET"
        self.run = RunMain(url=url,method=method)

    def test_01(self):
        url = 'https://www.imooc.com/course/ajaxcoursenewrecom?cid=9'

        res = self.run.run_main(url,'GET')
        print('这是第1个case')

        self.assertEqual(res['msg'],'成功','测试通过')


if __name__ == '__main__':
    filepath = "../report/HtmlReport.html"
    fp = open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))

    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="This is first report")
    runner.run(suite)
    fp.close()