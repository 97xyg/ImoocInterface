#coding=utf-8
import requests
import json
#上传文件
url = 'https://www.imooc.com/user/postpic'
file ={
    "fileField":("top.jpg",open("D:/picture/top.jpg","rb"),"image/jpg"),
    "type":"1"
}
cookie = {
    "apsid":"QzYjhmZWQyMDk2MmFlMzJhNjJkZTUxZDI2NzQ5ODMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODIyNzkyOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADI5MmU3OTQ2ZWZmNTM1N2YzNDQ4M2NkMTRiZmFhOWUAQQT%2BXUEE%2Fl0%3DND"
}
res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)





