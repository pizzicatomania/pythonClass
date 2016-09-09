# import threading
from threading import Thread, Lock
import time
lock = Lock()
mysum = 0 #임계영역
def thFn1( arg ):
    global mysum
    for n in range(1,6):
        with lock:
            mysum +=n
def thFn2( arg ):
    global mysum
    for n in range(6,11):
        with lock:
            mysum +=n
def main():
    th1 = Thread( target=thFn1, args=('mythread',) )
    th2 = Thread( target=thFn2, args=('mythread',) )
    th1.start()
    th2.start()
    
    th1.join()
    th2.join()
    print('mysum=', mysum)
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
# def genFn():
#     while True:
#         print('hello')
#         time.sleep(1) #1초간 잠시 멈춤
# def thFn( arg ):
#     while True:
#         print('hello')
#         time.sleep(1) #1초간 잠시 멈춤
# 
# class MyThread(Thread):
#     def run(self):
#         while True:
#             print('hello')
#             time.sleep(1) #1초간 잠시 멈춤
# 
# if __name__ == '__main__':
#     th = MyThread()
#     th.start() #run 함수를 thread call.
#     print('korea')

#     genFn()
#     th = Thread( target=thFn, args=('mythread',) )
#     th.start()
    
    
    



    
    
    
    
    
    
    
    
    