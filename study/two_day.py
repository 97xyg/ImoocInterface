#coding=utf-8
import requests
import json
#上传文件
#url = 'https://www.imooc.com/user/postpic'
#下载文件
download_url = 'http://file.mukewang.com/apk/app/109/imooc7.2.810102001android.apk?version=1574827098'
file ={
    "fileField":("top.jpg",open("D:/picture/top.jpg","rb"),"image/jpg"),
    "type":"1"
}
cookie = {
    "apsid":"QzYjhmZWQyMDk2MmFlMzJhNjJkZTUxZDI2NzQ5ODMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODIyNzkyOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADI5MmU3OTQ2ZWZmNTM1N2YzNDQ4M2NkMTRiZmFhOWUAQQT%2BXUEE%2Fl0%3DND"
}
res = requests.get(download_url)
with open("mukewang1.apk","wb") as f:
    f.write(res.content)
#res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)





