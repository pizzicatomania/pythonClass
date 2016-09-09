class Animal: #인터페이스
    def Live(self):
        pass
    def Die(self):
        pass
        
class Pet(Animal): #추상클래스...(1개 이상의 추상함수를 포함하는 경우) 객체
    def sleep(self):
        print("zzzz")
    def eat(self): #추상함수..  virtual void eat()=0, abstract void eat()
        pass
    
class Dog(Pet):
    def speak(self):
        print('bow wow')
    def eat(self): 
        print("bone")
        
class Cat(Pet):
    def speak(self):
        print('meow')
    def eat(self): 
        print("fish")
        
if __name__ == '__main__':
    dog = Dog()
    dog.sleep()
    dog.eat()
    dog.speak()    
    
    