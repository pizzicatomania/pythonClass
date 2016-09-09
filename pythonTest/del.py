class Test:
    a = 0
    b = 0
    def setData(self, x, y):
        print("self:", id(self))
        self.a = x
        self.b = y
    def show(self):
        print("self:", id(self))
        print(self.a, self.b)
    
if __name__== '__main__':
    obj = Test();
    print("obj:", id(obj))
    obj.a = 10
    obj.b = 20
    obj.setData(100, 200)
    obj.show()
    obj1 = Test()
    print("obj1:", id(obj1))
    obj1.setData(1000, 2000)
    obj1.show()
#     print (obj.a, obj.b)