#coding=utf-8
import sys
import os
#sys.path.append("D:/www/ImoocInterface/")
import unittest
#获取当前目录的绝对路径
case_path = os.getcwd()+"/UnittestCase/"
print(case_path)
'''
from UnittestCase.test_case01 import TestCase01
from UnittestCase.test_case02 import TestCase02
from UnittestCase.test_case03 import TestCase03
case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
suite = unittest.TestSuite()
tests = [case_01,case_02,case_03]
suite.addTests(tests)
runner = unittest.TextTestRunner()
runner.run(suite)
'''
discover = unittest.defaultTestLoader.discover(case_path)
runner = unittest.TextTestRunner()
runner.run(discover)
#print(discover)