#coding=utf-8
import sys
import os
base_path = os.getcwd()
import unittest
sys.path.append(base_path)
from Util.handle_excel import excel_data
import json
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Base.base_request import request
#['imooc_001', '登陆', 'yes', None, 'login', 'post', '{"username":"111111"}', 'yes', 'message', None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[6]
                url = data[5]
                data1 = data[7]
                expect_method = data[10]
                expect_result = data[11]
                res = request.run_main(method,url,data1)
                #print(res)
                code = str(res['errorCode'])
                message = res['errorDesc']
                if expect_method == 'mec':
                    config_message = handle_result(url,code)
                    if message == config_message:
                        excel_data.excel_write_data(i+2,13,"通过")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                if expect_method == 'errorcode':
                    if expect_result == code:
                        excel_data.excel_write_data(i+2,13,"通过")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                if expect_method == 'json':
                    if code == 1000:
                        status_str='sucess'
                    else:
                        status_str='error'
                    expect_result = get_result_json(url,status_str)
                    result = handle_result_json(res,expect_result)
                    if result:
                        excel_data.excel_write_data(i+2,13,"通过")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i+2,14,json.dumps(res))

if __name__ == "__main__":
    run =RunMain()
    run.run_case()