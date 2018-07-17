class Person(object):
    #I dont think you can create an empty default constructor in python, but 
    # @classmethod can be used for 
    def __init__(self, name=""):
        if not name:
            self.name = "Null"
        else:
            self.name = name


        
    def setName(self,name): 
        tempName = self.name
        self.name = name 
        return("I was "+tempName+ " now I go by "+self.name+".")
        
        
    def introduction(self):
        if self.name is "Null":
            return('I do not have a name')
        else:
            return('Hello my name is '+self.name)
        
class Student(object):
    def __init__(self,name):
        if not name:
            self.name = "Null"
        else:
            self.name = name
            
    def setName(self,name):
        tempName = self.name
        self.name = name
        return("Hello I am "+self.name+" and I am a student")


def assignName(personType):
    return personType.name
        

personObj = Person()
kionObj = Person("Kion")
studentObj = Student("Jack")

print(personObj.name)
print(kionObj.name)
print(studentObj.name)

print("++++++++++++++")
print(personObj.setName("Jeff"))
print(kionObj.setName("Null"))
print("++++++++++++++")

print(studentObj.setName("J A C K"))
print(personObj.introduction())
print(kionObj.introduction())
print("++++++++++++++")


print(assignName(personObj))
print(assignName(kionObj))
print(assignName(studentObj))





