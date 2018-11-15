#!!!Only compiled not actually tested
class Node:
    def __init__(self, data, nextNode):
        self.data = data #proably a better naming convetion for python
        self.nextNode = None
        
class linkedlist:
    #no overloaded constructors so using none here
    def __init__(self, Node=None):
        self.head = Node

    def inset(self, node):
        if self.head = None:
            self.head = node
        else:
           temp = self.head
           self.head = node
           self.head.NextNode = temp
        
    def delete ():
        
