#coding=utf-8
import json
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_json import get_value,read_json,write_value
#1、获取cookie
#2、写入cookie
#3、是否携带cookie
'''
data = {
        "app":{
            "aaaa":"bbbbbb"
            }
    }
'''
'''
{
        "aaaa":"bbbbbb"}
    }
'''
def get_cookie_value():
    data1 = {
            "aaaa":"bbbbbb"
        }
    data = read_json("/Config/cookie.json")
    data["web"] = data1
    write_value(data)

if __name__ == "__main__":
    get_cookie_value()