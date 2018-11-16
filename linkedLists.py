#!!!Only compiled not actually tested
class Node:
    def __init__(self, data, nextNode):
        self.data = data #proably a better naming convetion for python
        self.nextNode = None
        
class linkedlist:
    #no overloaded constructors so using none here
    def __init__(self, Node=None):
        self.head = Node

    def insetAtFirst(self, node):
        if self.head = None:
            self.head = node
        else:
           temp = self.head
           self.head = node
           self.head.NextNode = temp

    def findElement(self,element):
        #need to think about looping

    #there might be a problem here
    def delete (self,key):
        cur = self.hear
        while cur is not None:
            if cur.data == key:
                temp = cur.nextNode
                cur.nextNode = none
                
    def printList(self):
        cur = self.head
        while cur is not None:
            print( cur.data )
            cur = cur.nextNode
        
