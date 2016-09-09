# n = [n*10 for n in range(1,11)]
# n = [n for n in range(1,11) if n%2==0]
# print(n)

# my=[(10,'aaa'),(20,'aaa'), (30, 'ccc')]
# a={k:v for k,v in my}
# print(a)

# a1 = enumerate([10,20,30])
# a1 = dict(a1)
# print(a1)
# 
# a2=zip([10,20,30],['aaa','bbb','ccc'])
# a2= dict(a2)
# print(a2)

n=int(input('enter a integer number: '))
print([d for d in range(1,n+1) if n%d==0])


# n = 1
# while n<=5:
#     print(n)
#     n+=1


# myD = {'name':'dkkd','age':23,'dsad':'dasdas'}
# 
# for a,b in myD.items():
#     print(a,b)
#     
# rd = range(0,10,1)
# print(list(rd))
# 
# 
# for n in range(1,11):
#     print(n)