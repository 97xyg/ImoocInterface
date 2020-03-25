#coding=utf-8
import sys
import os
base_path = os.getcwd()
import unittest
sys.path.append(base_path)
from Util.handle_excel import excel_data
from Base.base_request import request

#['imooc_001', '登陆', 'yes', None, 'login', 'post', '{"username":"111111"}', 'yes', 'message', None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == 'yes'
                method = data[5]
                url = data[4]
                data1 = data[6]
                request.send_post(method,url,data1)

            print(data)

if __name__ == "__main__":
    run =RunMain()
    run.run_case()