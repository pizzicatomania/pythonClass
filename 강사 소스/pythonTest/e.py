import sys
a =[10,20,30]
c= b = a
print( sys.getrefcount(a)-1 )


# a =[10,20,30]
# # b =[10,20,30]
# # b = a #shallow copy
# b = a.copy() #deep copy
# a[0] =100
# print(id(a))
# print(id(b))
# print(b)

# a = 1021394719347123491273410234812340129348
# a =100
# b = a
# b = 1000
# print(id(a))
# print(id(b))
