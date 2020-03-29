#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

file_path = base_path+"/Config/server.ini"
cf = configparser.ConfigParser()
cf.read(file_path)
data = cf.get('server','host')
print(data)
