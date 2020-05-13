#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import ddt
import unittest
data = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]

@ddt.ddt
class TestCase01(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")
        
    @ddt.data(*data)
    def test_01(self,data1):
        casename,casenum,isrun,method,cookie = data1
        print("this is test case",casename,casenum,isrun,method,cookie)

if __name__ == "__main__":
    unittest.main()



