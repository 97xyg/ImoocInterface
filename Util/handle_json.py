#coding=utf-8
import json
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

def read_json(file_name=None):
    if file_name == None:
        file_path = base_path+"/Config/user_data.json"
    else:
        file_path = base_path+file_name
    with open(file_path,encoding='UTF-8') as f:
        data = json.load(f)
    return data

def get_value(key,file_name=None):
    data = read_json(file_name)
    #return data[key]
    return data.get(key)

def write_value(data):
    data_value = json.dumps(data)
    with open(base_path+"/Config/cookie.json","w") as f:
        f.write(data_value)

if __name__ == "__main__":
    data = {
        "app":{
            "aaaa":"bbbbbb"}
    }
    write_value(data)
