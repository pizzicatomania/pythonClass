class Test:
    def __init__(self, x=0, y=0):
        print("init call.")
        self.a =x
        self.b =y
    def setData(self, x, y): #멤버함수...
        self.a = x
        self.b = y
    def show(self):
        print(self.a,self.b)

if __name__ == '__main__':
    obj = Test(10,20) #객체생성( 멤버데이터의 초기화를 자동호출되는 함수(생성자함수)
    obj.show()
    obj1 = Test()
    
    
    
    