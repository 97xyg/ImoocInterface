#coding=utf-8
import json
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

def read_json():
    with open(base_path+"/Config/user_data.json") as f:
        data = json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]
