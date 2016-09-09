class Test:
    def __init__(self, x=0, y=0):
        print('init called')
        self.a=x
        self.b=y

    def setData(self, x, y):
        self.a = x
        self.b = y
    
    def show(self):
        print(self.a, self.b)
    
if __name__== '__main__':
    obj = Test(10,20);
    obj.show();
    obj1=Test()