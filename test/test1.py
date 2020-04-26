import hashlib


dic = {"name":"ace",'age':120}

m = hashlib.md5(str(dic).encode('utf-8')).hexdigest()

dic['hash'] = m

print(dic)


dis = (1048, u'\u6eda\u86cb\u5427\uff01\u80bf\u7624\u541b', '')


print(dis[2] == None)
print(dis[2] is None)

print(not dis[2] is None)
print(dis[2] == '')