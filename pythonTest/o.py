class People:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def setName(self, name):
        self.name= name
    
class Student(People):
    
    def __init__(self,name,age,stdNum):
        super().__init__(name,age)
        self.stdNum= stdNum
    
    def setStdNum(self, stdNum):
        self.stdNum = stdNum
    
if __name__ == '__main__':
    std = Student('asdasd',31,412412)
    print(std.name, std.age, std.stdNum)