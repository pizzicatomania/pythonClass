num1 = int( input("숫자1:") )
num2 = int( input("숫자2:") )

# num1 = -1*num1 if num1<0 else num1
num1 = (num1,-num1)[ num1<0 ]
num1 = {False:num1,True:-num1}[ num1<0 ]
# num2 = -num2 if num2<0 else num2
num2 = (num2,-num2)[ num2<0 ]
print("절대값의합:", num1+num2 )
# n =input('입력:')
# n = int(n)
# print(n)
# print(type(n))

# int n=3;
# int result = n>0? 100:200;
# n =-3
# # result = 100 if n>0 else 200
# # result = (100,200)[ n>0 ]
# result ={True:100, False:200}[n>0]
# print(result)

# n =0
# if n>0:
#     print('positive')
# elif n<0:
#     print('negative')
# else:
#     print('zero')
# print('hello')