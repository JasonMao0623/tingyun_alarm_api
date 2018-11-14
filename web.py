from flask import Flask,request
app =Flask(__name__)
import time
import json
@app.route("/alarm",methods=["POST"])
# 测试环境方法
def test_dataProcess():
    if request.method =="POST":
        # print(request.form)
        a = request.data
        print(str(a, encoding = "utf-8"))
        # dict1 = json.loads(str(a, encoding = "utf-8"))
        # print(dict1)
        return  "ok"
    else:
        return "请求方法为POST",500
app.run(
    host="0.0.0.0",
    port = 10080,
    debug=True
)