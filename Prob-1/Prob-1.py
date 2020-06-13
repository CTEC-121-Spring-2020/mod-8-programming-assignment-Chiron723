# Module 8
#   Programming Assignment 11
#     Prob-1.py

# Your code below
class car:
    def __init__(self, make, model, year):
        self._make=make
        self._model=model
        self._year=year

    def set_make(self,make):
        self._make=make

    def get_Make(self):
        return self._make
    
    def set_model(self,model):
        self._model=model
        
    def get_model(self):
        return self._model

    def set_year(self,year):
        self._year=year
    
    def get_year(self):
        return self._year
    
def TestCar():
    autoLot=[]
    autoLot.append(car("make\t", "model\t", "year"))
    autoLot.append(car("Toyota\t","Corola",1984))
    autoLot.append(car("Mercury","Sable\t", 1995))
    autoLot.append(car("Datsun\t","Cherry\t", 1975))
    autoLot.append(car("DMC\t","Delorian",1984))
    autoLot.append(car("Volkswagon","Beetle",1970))
    for i in range(len(autoLot)):
        print(autoLot[i].get_Make(),"\t",autoLot[i].get_model(),"\t",autoLot[i].get_year())

if __name__ == "__main__":
    TestCar()

