#coding=utf-8
import sys
sys.path.append("D:/www/ImoocInterface/")
import unittest
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