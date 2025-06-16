#  dobly linked list

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinked:
    def __init__(self):
        self.head =  None

    def traverse(self):
        temp = self.head
        while temp!=None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def delAtIndex(self, index):
        if self.head == None:
            return
        if self.head.next == None:
            if index == 0:
                self.head = None
            return
        count = 0
        temp = self.head
        while temp != None:
            if count == index:
                break;
            count = count + 1
            temp = temp.next
        if temp == None:
            return
        if temp.next == None:
            temp.prev.next = None
        elif temp.prev == None:
            self.head = temp.next
            temp.next.prev = None
        else : 
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            # temp.prev
        print("data to be deleted", temp.data)
    
    def addAtIndex(self, data, index):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return 

        count = 0
        temp = self.head
        if index == 0:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            return
        while temp != None:
            if count == index - 1:
                break
            count = count + 1
            temp = temp.next
        
        if temp == None:
            return
        if temp.next != None:
            a = temp.next
            temp.next = newnode
            newnode.next = a
            a.prev = newnode
            newnode.prev = temp
        else:
            temp.next = newnode
            newnode.prev = temp

d = DoublyLinked()
d.addAtIndex(5, 0)
d.addAtIndex(50, 1)
d.addAtIndex(0, 2)
d.addAtIndex(6, 0)
d.addAtIndex(60, 1)
d.addAtIndex(600, 2)
d.addAtIndex(60, 6)
d.addAtIndex(160, 6)
d.traverse()
d.delAtIndex(2)
d.traverse()
d.delAtIndex(0)
d.traverse()
d.delAtIndex(0)
d.traverse()