class Person:

    
    #I dont think you can create an empty default constructor in python, but 
    # @classmethod can be used for 
    def __init__(self, name=""):
        if not name:
            self.name = "Null"
        else:
            self.name = name


        
    def assignName(self,name): 
        tempName = self.name
        self.name = name 
        return("I was "+tempName+ " now I go by "+self.name+".")
        
        
    def introduction(self):
        if self.name is "Null":
            return('I do not have a name')
        else:
            return('Hello my name is '+self.name)
            

personObj = Person()
kionObj = Person("Kion")

print(personObj.name)
print(kionObj.name)

print(personObj.assignName("Jeff"))
print(kionObj.assignName("Null"))

print(personObj.introduction())
print(kionObj.introduction())





