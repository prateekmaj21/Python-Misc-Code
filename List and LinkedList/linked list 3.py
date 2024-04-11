# A single node of a singly linked list

class Node:
    #constructor
    def __init__(self, data=None, next=None):
        self.data= data
        self.next= next
        
# a linked list class with a single head Node
class LinkedList:
    def __init__(self):
        self.head= None
        
#insertion method for a linked list

    def insert(self, data):
        newNode= Node(data)
        if (self.head):
            current=self.head
            while( current.next):
                current= current.next
            current.next = newNode
        else:
            self.head= newNode

    def printLinkedList( self):
        current= self.head
        while(current):
            print(current.data)
            current= current.next
            
# Singly Linked List with insertion and print methods

LL= LinkedList()
LL.insert(350)
LL.insert(400)
LL.insert(500)
LL.insert(600)
LL.printLinkedList()
        
