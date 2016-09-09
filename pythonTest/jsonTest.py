import json

fp = open('my.json','r',encoding='utf-8')
myD = json.load(fp)
print(type(myD))
print(myD)


# myj = '[{"name":"aaa", "age":20},{"name":"bbb", "age":20}]'
# myD = json.loads(myj)
# print(type(myD))
# print(myD)
# for d in myD:
#     print(d['name'], d['age'])

# myD=[{'name':'aaa', 'age':20},{'name':'bbb', 'age':22},{'name':'ccc', 'age':30}]
# fp = open('my1.json','w',encoding='utf-8')
# str1 = json.dumps(myD, fp, ensure_ascii=False)

# print(type(str1))
# print(str1)
# 
# fp= open('my.json','w',encoding='utf-8')
# fp.write(str1)
# fp.close()