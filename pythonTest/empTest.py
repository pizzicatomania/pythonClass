class Employee:
    def __init__(self, name, addr):
        self.name= name
        self.addr = addr
    def ShowYourName(self):
        print("name:", self.name)
    def ShowYourAddr(self):
        print("addr:", self.addr)
    def empProc(self):  #template method
        self.ShowYourName()
        self.ShowYourAddr()
        self.ShowSalaryInfo()
    def GetPay(self):
        pass
    def ShowSalaryInfo(self):
        pass
class Permanent(Employee):
    def __init__(self, name, addr, salary):
        super().__init__(name, addr)
        self.salary = salary
    def GetPay(self):
        return self.salary
    def ShowSalaryInfo(self):
        print("영구직연봉:", self.salary) # self.GetPa()
class Temporary(Employee):
    def __init__(self, name, addr, day,pay):
        super().__init__(name, addr)
        self.day = day
        self.pay = pay
    def GetPay(self):
        return self.day * self.pay
    def ShowSalaryInfo(self):
        print("임시직급여:", self.GetPay() ) # self.GetPa()
class Manager(Employee):
    def __init__(self, name, addr, salary, dept):
        super().__init__(name, addr)
        self.salary = salary
        self.dept = dept
    def GetPay(self):
        return self.salary
    def ShowSalaryInfo(self):
        print("관리자급여:", self.GetPay(), " 부서:",self.dept ) # self.GetPa()

class EmpProcContext:
    def changeStrategy(self ,emp):
        self.emp = emp
    def contextEmpInfo(self):
        self.emp.ShowYourName()
        self.emp.ShowYourAddr()
        self.emp.ShowSalaryInfo()
if __name__ == '__main__':
    p = Permanent("홍길동","서울시 은평구", 7000)
    p.empProc()
    p = Temporary("임꺽정","부산시", 5,500)
    p.empProc()
#     context = EmpProcContext()
#     context.changeStrategy(Permanent("홍길동","서울시 은평구", 7000))
#     context.contextEmpInfo()
#     context.changeStrategy(Temporary("임꺽정","부산시", 5,500))
#     context.contextEmpInfo()
#     context.changeStrategy(Manager("김철수","광주시", 9000, "개발"))
#     context.contextEmpInfo()





# def empInfo( emp ): #공통로직
#     emp.ShowYourName()
#     emp.ShowYourAddr()
#     emp.ShowSalaryInfo()
#     
# if __name__ == '__main__':
#     empInfo(Manager("김철수","광주시", 9000, "개발"))
#     empInfo(Permanent("홍길동","서울시 은평구", 7000))
#     empInfo(Temporary("임꺽정","부산시", 5,500))
    
    
#     p = Manager("김철수","광주시", 9000, "개발")
#     p.ShowYourName()
#     p.ShowYourAddr()
#     p.ShowSalaryInfo()
#     
#     p = Permanent("홍길동","서울시 은평구", 7000)
#     p.ShowYourName()
#     p.ShowYourAddr()
#     p.ShowSalaryInfo()
#     p = Temporary("임꺽정","부산시", 5,500)
#     p.ShowYourName()
#     p.ShowYourAddr()
#     p.ShowSalaryInfo()




















