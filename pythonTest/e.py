import sys
a=[10,20,30]
c=b=a
print(sys.getrefcount(a)-1)

# a=[100]
# b=a.copy()
# 
# print(id(a))
# print(id(b))