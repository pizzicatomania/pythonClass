import socket
import json
svrSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM ) #create
svrSock.bind( ("", 5500) )
svrSock.listen(5)
print("client wait...")
dataSock,addr = svrSock.accept() # hang....
print("client connect", addr)

rdata = dataSock.recv(100)
sdata = str(rdata,'utf-8')
dictData = json.loads(sdata)
print(dictData['name'], dictData['age'] )


# while True:
#     try:
#         rdata = dataSock.recv(100) #hang..(동기소켓)
#         if not rdata:
#             break
#         sdata = str(rdata,'utf-8')
#         print("recv:", sdata )
#         dataSock.send( bytes( sdata,'utf-8') ) 
#     except Exception as err:
#         print("client close")
#         dataSock.close()
#         break;
#     
# print("server end..")






