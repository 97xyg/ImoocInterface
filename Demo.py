import requests

data = {
    'username':'mushishi',
    'password':'111111'
}

res = requests.post(url='http://127.0.0.1:8888/login/',data=data)
print(res.text)