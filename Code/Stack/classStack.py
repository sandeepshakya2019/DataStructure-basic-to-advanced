class Stack:
    def __init__(self):
        self.__arr = []

    def push(self, elem):
        self.__arr.append(elem)

    def pop(self):
        if self.isEmpty():
            print("No element to pop")
            return None
        return self.__arr.pop() 

    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.__arr[-1]  

    def isEmpty(self):
        return len(self.__arr) == 0

    

s = Stack()
s.push(8)