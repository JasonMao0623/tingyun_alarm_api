#字符串转json，拼接新标准json格式body
def strToJson(data):
    dict_data = data
    tmp_data = {}
    for index in dict_data:
        key = index["name"]
        value = index["value"]
        tmp_data[key] = value
    return tmp_data

