# Module 8
#   Programming Assignment 11
#     Prob-2.py

# Your code below
class Student:
    """I chose to focus on name and ID number because in any 
    school setting those are almost always the two most 
    important details, the major and gpa are generally the 
    details that you are searching for anyways"""
    def __init__(self,name,IDNumber):
        self._name=name
        self._IDNumber=IDNumber
        self._major=""
        self._gpa=0.0
        
    def set_name(self,name):
        self._name=name
    
    def get_name(self):
        return self._name
    
    def set_IDNumber(self,IDNumber):
        self._IDNumber=IDNumber
    
    def get_IDNumber(self):
        return self._IDNumber

    def set_major(self, major):
        self._major=major
    
    def get_major(self):
        return self._major
    
    def set_gpa(self,gpa):
        self._gpa=gpa
    
    def get_gpa(self):
        return self._gpa

def TestClass():
    records=[]
    records.append(Student("Joe Bella\t",9933))
    records.append(Student("Tucker Blank\t",3399))
    records.append(Student("Gayle Ujifusa\t",1011))
    records.append(Student("Edna Anker\t",9875))
    records[0].set_major("Web Development")
    records[1].set_major("Nursing")
    records[2].set_major("Baking")
    records[3].set_major("Medical Office")
    records[0].set_gpa(3.8)
    records[1].set_gpa(3.0)
    records[2].set_gpa(2.8)
    records[3].set_gpa(3.0)
    
    for i in records:
        print(i.get_name())
        print(i.get_IDNumber())
        print(i.get_major())
        print(i.get_gpa())
        
if __name__ == "__main__":
    TestClass()