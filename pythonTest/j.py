def fn():
    print('hello')
    print('world')

def addd(a,b):
    return a+b;

def fn1():
    return 10, 20;

def fn2(a=10, b=20, c=30):
    print(a,b,c)

def fn3(a,b):
    print(a,b)

def fn4(a, *arg):
    print(arg)
    for n in arg:
        print (n) 
    
    
def fn5(**arg):
    print(arg)
    
myD={"name":"aaa", "age":20, "add":"dasd"}
fn5(name="aaa", age=20, add="dasd")
fn5(a=1)
fn5(**myD)
    
# fn3(b=10,a=20)
# fn4(10,20,30,40,50,60)
# fn4('asdasdsad','asdsd')

# 
# def shape(r,h,w):
#     return r**2*3.14, h*w
# 
# circle, rect = shape(3, 10, 20)
# print(circle, rect);
# 
# fn2();
# fn2(c=40,a=0)
# 
# fn()
# fn()
# 
# res = fn1();
# print(res)