#Start with a single node

class Node:
    #constructor
    def __init__(self, data, next=None):
        self.data=data
        self.next= next
        
        
a= Node(45)
b=Node(57)
val1=Node("name")

print(a.data)
print(b.data)
print(val1.data)