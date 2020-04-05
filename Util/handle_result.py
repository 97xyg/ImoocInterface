#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import json
from Util.handle_json import get_value
print(get_value("api3/getbanneradvertver2","/Config/code_message.json"))