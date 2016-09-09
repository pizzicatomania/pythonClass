import json

fp = open("my.json",'r',encoding='utf-8')
myD = json.load(fp)
print(type(myD))
print(myD)
for data in myD:
    print("%(name)s %(age)d"%data )

# myj='[{"name":"홍길동","age":20},{"name":"임꺽정","age":20}]'
# myD = json.loads( myj)
# print(type(myD))
# print(myD)
# for data in myD:
#     print("%(name)s %(age)d"%data )
# print(myD['name'], myD['age'])


# myD=[{'name':'홍길동','age':20},{'name':'임꺽정','age':30},{'name':'이순신','age':40}]
# fp = open("my1.json",'w', encoding='utf-8')
# str1 = json.dump(myD, fp, ensure_ascii=False)
# str1 = json.dumps(myD, ensure_ascii=False)
# print(type(str1))
# print(str1)
# fp = open("my.json",'w', encoding='utf-8')
# fp.write( str1 )
# fp.close()