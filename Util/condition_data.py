#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import excel_data

def split_data(data):
    #imooc_005>data:banner:id
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data

def depend_data(data):
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id)
    data = excel_data.get_cell_value(row_number,14)
    return data

if __name__ == "__main__":
    print(depend_data("imooc_007>data:banner:id"))

    
