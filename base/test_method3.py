#coding = utf-8
import unittest
import HTMLTestRunner
from demo1 import RunMain

class TestMethod(unittest.TestCase):
    def setUp(self):
        url = 'https://www.imooc.com/passport/user/login'
        method = "POST"
        self.run = RunMain(url=url,method=method)

    def test_01(self):
        url = 'https://www.imooc.com/passport/user/login'
        data = {
            'username':'18365031085',
            'password':'wx1vr/0lfIMYd22cIrsMVynFEJkW/Q2Q3+veli2QXQIRJ5XOnXCDCFyDIG8V4Lk1gYS4rRhlzP59f54QugNoXP0/Giuo9pBeG1O7rC9vOU4EsnAHzL2XOPZbvDbg7JyDIVE/5+Z/+wwnNunh5sbVrPrKbMkQj1Jw5JcxQoU90ak=',
            'verify':'',
            'remember':'1',
            'pwencode':'1',
            'browser_key':'9690e32abb49ff8c4ef30cbec064c3cd',
            'referer':'https://www.imooc.com'
        }

        res = self.run.run_main(url,'POST',data)
        print('这是第1个case')

        #self.assertEqual(res['msg'],'成功','测试通过')


if __name__ == '__main__':
    filepath = "../report/HtmlReport.html"
    fp = open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))

    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="This is first report")
    runner.run(suite)
    fp.close()