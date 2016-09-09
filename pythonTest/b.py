a = b'abcde'
ba = bytearray(a)

print(type(ba))
print(ba)

# ba[1]=ord('G')
ba[1]=65 #'A'

print(ba)


# a= False + 1
# print(type(a))
# print(a)

# a= b'abcdefghijk'
# b="bbbb"
# 
# print(type(a))
# print(a)
# 
# # a = str(a,'utf-8');
# a=a.decode('utf_8')
# 
# print(type(a))
# print(a)
# print('======================')
# print(type(b))
# print(b)
# b = bytes(b,'utf-8')
# print(type(b))
# print(b)