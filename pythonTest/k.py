def fn():
    print("fn called")
    
def fn1():
    print("fn1 called")
    
myDic = {1:fn, 2:fn1}
myDic[1]()
myDic[2]()
    
# my = fn
# print(id(my))
# print(id(fn))
# my()


# print(dir(__builtins__))
# 
# # str = "abc"
# 
# def fn():
#     str="def"
#     print(str)
#     
# fn()
# print(str)
# 
# a= str(100)

# g=100
# 
# def fn():
# #     global g
#     g = 10
#     print("g=",g)
#     
# fn()
# print("g=",g)