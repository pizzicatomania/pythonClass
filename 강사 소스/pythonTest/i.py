a = 10
b = 3.141592
c = "abc"
s1 = "a=%10d b=%.2f c=%s" % (a,b,c)
print(s1)

myD = {'name':'aaa','age':20,'addr':'bbb'}
s2 ="이름:%(name)s 나이=%(age)d 주소=%(addr)s" % myD
print(s2)

s3 = "a={0:10} b={1:.2f} c={2:>10}".format(a,b,c)
print(s3)

s4 ="이름:{name} 나이={age} 주소={addr}".format( **myD )
print(s4)











