from threading import Thread, Lock
import time
lock = Lock()
       
mysum = 0
def thFn1(arg):
    global mysum
    for n in range(1,6):
        with lock:
            mysum += n
        
def thFn2(arg):
    global mysum
    for n in range(6,11):
        with lock:
            mysum += n
    

def main():
    th1 = Thread(target=thFn1, args=('asd',))
    th2 = Thread(target=thFn2, args=('asd',))
    th1.start()        
    th2.start()
    th1.join()
    th2.join()
    
    print(mysum)
        
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
# class MyThread(Thread):
#     def run(self):
#         while True:
#             print('hello')
#             time.sleep(1)
            
#         
# if __name__ == '__main__':
#     th = MyThread()
#     th.start()
#     
# #     genFn()
# 
# #     th = Thread(target=thFn, args=('mmmmmm',))
# #     th.start()
#     print('ddddd')