class FriedRice:
    def Fry(self):
        print("Fry Rice")
        
    def CookingProc(self):
        self.InputSeasoning();
        self.Fry()
        
    def InputSeasoning(self):
        pass
    
    
class KimchiFriedRice(FriedRice):
    def InputSeasoning(self):
        print('input kimchi')
        

class ShrimpFriedRice(FriedRice):
    def InputSeasoning(self):
        print('input shrimp')
        
        
if __name__ == '__main__':
    p_rice= ShrimpFriedRice()
    p_rice.CookingProc()
    p_rice= KimchiFriedRice()
    p_rice.CookingProc()