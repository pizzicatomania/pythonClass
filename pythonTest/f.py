# n = 1
# # result = 100 if n>0 else 200
# # result = (100,200)[n > 0]
# result = {True: 100, False:200} [n>0]
# print(result)

# if n > 0:
#     print('p')
# elif n < 0:
#     print('n')
# else:
#     print('z')
# print('hello')

a=int(input('enter first number: '))
b=int(input('enter second number: '))

a= -a if a<0 else a
b= -b if b<0 else b

print(a+b)