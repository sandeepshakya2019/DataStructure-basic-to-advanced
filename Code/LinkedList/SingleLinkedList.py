class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.data, sep=" ", end=" ")
            temp = temp.next
        print()

    def addAtEnd(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newnode
    
    def addAtstart(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            newnode.next = temp
            self.head = newnode

    def deleteAtIndex(self, index):
        count = 0
        if self.head == None: return 
        temp = self.head
        prev = None
        nex = None
        if self.head.next == None:
            if index == 0:
                self.head = None
                return 
        while (temp != None):
            # print(temp, count, index)
            if count == index - 1:
                prev = temp
            elif count == index + 1:
                nex = temp

            count = count + 1
            temp = temp.next
    
        if prev != None :
            prev.next = nex
        elif prev == None and nex != None:
            self.head = nex
        else:
            return
        
    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        curr_node = self.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node =curr_node
            curr_node = next_node
        self.head = prev_node

    def middle(self):
        if self.head == None:
            return 
        if self.head.next == None:
            return self.head
        
        slow = self.head
        fast = slow

        while fast != None and fast.next !=None:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None
        
        print(slow.data)

    def reversestartend(self, start, end):
        print("get data", start.data, end.data)
        prev = None
        curr = start

        if curr is None or curr == end:
            return curr

        while True:
            # print(1)
            next_node = curr.next
            curr.next = prev
            prev = curr
            if curr == end:
                break
            curr = next_node

        # 'start' now becomes the tail of the reversed section
        start.next = next_node  # Connect tail of reversed section to the rest
        return prev  # This is the new head of the reversed section



    def removeduplicate(self, head):
        map = {}
        temp = head
        while temp is not None:
            if temp.data not in map:
                map[temp.data] = 1
            temp = temp.next
        temp = head
        print(len(map))
        c = 0
        for i in map:
            c = c + 1
            temp.data = i
            if c <= len(map) - 1:
                temp = temp.next
        temp.next = None


        

    

ll1 = SingleLinkedList()
ll1.addAtEnd(1)
ll1.addAtEnd(2)
ll1.addAtEnd(3)
ll1.addAtEnd(2)
ll1.addAtEnd(6)
# ll1.addAtEnd(6)
ll1.traverse()
# ll1.reverse()
# ll1.traverse()
# ll1.middle()
ll1.removeduplicate(ll1.head)
ll1.traverse()

# ll1.traverse()





