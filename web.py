from flask import Flask,request
app =Flask(__name__)
from urllib.parse import unquote
import json
import process
from flask import jsonify
@app.route("/alarm",methods=["POST"])
#定义路由
def test_dataProcess():
    if request.method =="POST":
        old_data = request.data
        #生产数据，生产环境请解开注释
        # new_data = unquote(str(old_data, encoding = "utf-8"))
        #测试假数据，生产环境请注释
        a = "%5B%7B%22name%22%3A%22name%22%2C%22value%22%3A%22Java+Application%22%7D%2C%7B%22name%22%3A%22metricname%22%2C%22value%22%3A%22%E5%BA%94%E7%94%A8%E5%93%8D%E5%BA%94%E6%97%B6%E9%97%B4%22%7D%2C%7B%22name%22%3A%22alarmtype%22%2C%22value%22%3A%221%22%7D%2C%7B%22name%22%3A%22content%22%2C%22value%22%3A%22%E5%BA%94%E7%94%A8%E5%93%8D%E5%BA%94%E6%97%B6%E9%97%B4%E8%B6%85%E8%BF%87%E9%98%88%E5%80%BC%EF%BC%8C%E5%91%8A%E8%AD%A6%22%7D%2C%7B%22name%22%3A%22endtime%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22persisttime%22%2C%22value%22%3A%22%E8%B6%85%E8%BF%871%E5%88%86%E9%92%9F%22%7D%2C%7B%22name%22%3A%22starttime%22%2C%22value%22%3A%222018-11-14+21%3A10%22%7D%2C%7B%22name%22%3A%22metricvalue%22%2C%22value%22%3A%2228.058823529411764%22%7D%2C%7B%22name%22%3A%22thresholdvalue%22%2C%22value%22%3A%221.0%22%7D%5D"
        new_data = unquote(a)
        res = process.strToJson(json.loads(new_data))
        return  jsonify(res)
    else:
        return "请求方法为POST",500
app.run(
    host="0.0.0.0",
    port = 10080,
    #生产环境请设置为False
    debug=False
)
