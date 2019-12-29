#coding=utf-8
import json
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/")
def Home():
    data = json.dumps({
        "username":"Mushishi_xu",
        "password":"111111"
    })
    return data

@app.route('/passport/user/login',methods=['GET'])
def Login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:
        data = json.dumps({
            "username": username,
            "password": password,
            "code":"200",
            "message":"登录成功",
            "info":"www.baidu.com"
        })
    else:
        data = json.dumps({
            "message":"请传参数"
        })

    return data

@app.route('/passport/user/post_login',methods=['POST'])
def post_login():
    request_method = request.method
    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        data = json.dumps({
            "username": username,
            "password": password,
            "code": "200",
            "message": "登录成功",
            "info": "www.Imooc.com"
        })
    else:
        data = json.dumps({
            "messsage":"请求不合法"
        })
    return data




#https://www.imooc.com/passport/user/login?username=Mushishi_xu@163.com&password=111111
if __name__ == "__main__":
    app.run()
