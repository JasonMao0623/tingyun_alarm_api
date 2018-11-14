from flask import Flask,request
app =Flask(__name__)
import time
@app.route("/alarm",methods=["POST"])
# 测试环境方法
def test_dataProcess():
    if request.method =="POST":
        print(request.form)
        return  "ok"
    else:
        return "请求方法为POST",500
app.run(
    host="0.0.0.0",
    port = 10080,
    debug=True
)