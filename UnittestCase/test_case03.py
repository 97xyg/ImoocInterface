#coding=utf-8
import requests
import unittest
url = "http://www.imooc.com"
data = {
    "username":"1111",
    "password":"222222"
}
class TestCase03(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case结束执行")

    @classmethod
    def setUpClass(cls):
        print("case类开始执行")

    @classmethod
    def tearDownClass(cls):
        print("case类执行结束")

    def test_07(self):
        print("执行case07")
        flag = "abcdefgaabdedg"
        s = "aabd"
        self.assertIn(s,flag,msg="不包含")

    def test_01(self):
        print("执行case01")
        #res = requests.get(url=url,params=data).json()
        data1 = {
            "user":"11111"
        }
        self.assertDictEqual(data1,data)

    def test_02(self):
        print("执行case02")
        data1 = {
            "username":"1111",
            "password":"222222"
        }
        self.assertDictEqual(data1,data,msg="这两个字典不相等")

    def test_03(self):
        print("执行case03")
        flag = True
        self.assertFalse(flag,msg="不等于True")

    def test_04(self):
        print("执行case04")
        flag = False
        self.assertTrue(flag,msg="不等于False")

    def test_05(self):
        print("执行case05")
        flag = "111"
        flag = "2222"
        self.assertEqual(flag,flag1,msg="两个字符串不相等")

    def test_06(self):
        print("执行case06")
        flag = "abcdefgaabdedg"
        s = "aabd"
        self.assertIn(s,flag,msg="不包含")

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    '''
    suite.addTest(TestCase03('test_06'))
    suite.addTest(TestCase03('test_04'))
    suite.addTest(TestCase03('test_02'))
    suite.addTest(TestCase03('test_05'))
    suite.addTest(TestCase03('test_01'))
    suite.addTest(TestCase03('test_07'))
    tests = [TestCase03('test_06'),TestCase03('test_04'),TestCase03('test_02'),TestCase03('test_05'),TestCase03('test_01'),TestCase03('test_07')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
