class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        head = self.head
        while temp.next!=head:
            print(temp.data, end= "->")
            temp = temp.next
        print(temp.data)
    
    def addAtStartOrEnd(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            newnode.next = newnode
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        print("d", temp.data, data)
        temp.next = newnode
        newnode.next = self.head
        self.head = newnode
    
c = CircularLinkedList()
c.addAtStartOrEnd(10)
c.addAtStartOrEnd(5)
c.addAtStartOrEnd(15)
c.addAtStartOrEnd(20)
c.traverse()



        
    

