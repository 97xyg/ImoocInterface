#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

class HandleInit:

    def load_ini(self):
        file_path = base_path + "/Config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8-sig")
        return cf

    def get_value(self,key,section=None):
        #获取ini里面的value
        if section == None:
            section = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(section,key)
        except Exception:
            print("没有获取到值")
            data = None
            
        return data

if __name__ == "__main__":
    hi = HandleInit()
    print(hi.get_value("password"))
