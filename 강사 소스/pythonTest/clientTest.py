import socket
import time
import json
dataSock = socket.socket(socket.AF_INET, 
                        socket.SOCK_STREAM ) #create
dataSock.connect( ('127.0.0.1',5500) )

sData ={'name':'홍길동','age':20 }
ssData = json.dumps( sData,ensure_ascii=False )
dataSock.send(  bytes(ssData,'utf-8') )
dataSock.close()
print("end client...")


# for n in range(0,3):
#     indata = input("입력:")
#     dataSock.send(  bytes(indata,'utf-8') )
#     rdata = dataSock.recv(100)
#     print("recv:",str(rdata,'utf-8') )
    

# time.sleep(3)
# dataSock.send( b'hello' )