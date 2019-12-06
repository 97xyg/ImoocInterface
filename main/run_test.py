#coding:utf-8
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
import sys
sys.path.append("D:\\www\\ImoocInterface")

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    #程序执行的主入口
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            expect = self.data.get_expect_data(i)
            header = self.data.is_header(i)
            if is_run:
                res = self.run_method.run_main(method,url,data,header)
                if util.common_util.is_contain(expect,res):
                    print("测试通过")
                else:
                    print("测试失败")

            return res
if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())






