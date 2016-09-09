class Test:
    a = 0  #멤버데이터..
    b = 0
    def setData(self, x, y): #멤버함수...
        print("self:", id(self) )
        self.a = x
        self.b = y
    def show(self):
        print("self:", id(self) )
        print(self.a,self.b)

if __name__ == '__main__':
    obj = Test()  #객체생성
    print("obj:", id(obj) )
    obj.a = 10
    obj.b = 20
    obj.setData(100, 200)
    obj.show()
    obj1 = Test()
    print("obj1:", id(obj1) )
    obj1.setData(1000, 2000)
    obj1.show()






