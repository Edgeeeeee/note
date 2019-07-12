import cgi,cgitb,json,time
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers  



# 接收用户发送的数据
fs = cgi.FieldStorage()
# 数据重组
inputs = {}  
for key in fs.keys():  
    inputs[key] = fs[key].value  


# 给用户返回数据
# print(inputs)
# print('1')

# time.sleep(3);

# 转换成json格式的数据
print(json.dumps(inputs))
# print(json.dumps([1,2,3]))
# print(inputs);
# print(fs,inputs);
# print('sucess')

