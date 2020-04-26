#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

def split_data(data):
    #imooc_005>data:banner:id
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data

    
