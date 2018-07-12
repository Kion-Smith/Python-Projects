class Person:
    name = "null"  
    def assignName(self,userInput): #Need to make sure to use self
        name = userInput # does not work, looking into fixing this
        print("Hello I am now know as "+userInput+".")
        
    def introduction(self):
        if name is 'null':
            print('I do not have a name')
        else:
            print('Hello my name is'+name)
            

personObj = Person()
print(personObj.name)
personObj.assignName('Kion')  

