def fn():
    print('hello')
    print('korea')

def hap(a,b):
    return a+b

def fn1():
    return 10,20 

def shape(r, h, w):
    return r**2*3.14, h*w

def fn2(a,b=20,c=30):
    print(a,b,c)
    
def fn3(a,b):
    print(a,b)

def fn4(*arg):
    print(arg)
    for n in arg:
        print(n)
    
def fn5( **arg ):
    print(arg)
myD={'name':'홍길동','age':30,'addr':'서울시'}    
fn5( name="aaa",age=20,addr="ccc" )
fn5( **myD )
    
    
fn4(10,20,30,40)
# fn4( 10,20,30,40 )


# fn3(10,20)
# fn3( b=100, a=200 )


# fn2()
# fn2(100)
# fn2(100,200)
# fn2(100,200,300)

# rst = fn1()
# print(rst )
# circle, rect = shape(3, 10, 20)
# print(circle, rect)

# fn()
# fn()
# rst = hap(10,20)
# print(rst)








