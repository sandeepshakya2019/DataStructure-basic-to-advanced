from collections import deque

class Queue:
    def __init__(self, size):
        self.q = [i for i in range(size)]
        self.size = size
        self.front = -1
        self.rear = -1

    def push(self, item):
        # self.q.append(item)  # Adds to the rear
        if self.rear == self.size : return "Queue is Full"
        if self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.q[self.front] = item
        else:
            self.rear += 1
            self.q[self.rear] = item
        

    def pop(self):
        if self.front == self.rear:
            return "Queue is Empty"
        else:
            popElem = self.q[self.front]
            self.front += 1
            if self.front == self.rear :
                self.front = -1
                self.rear = -1
            return popElem

    def size(self):
        # return len(self.q)
        if self.front == self.rear : return 0
        return self.rear - self.front + 1

    def empty(self):
        # return len(self.q) == 0
        return self.size() == 0

    def getFront(self):
        if self.front != -1:
            return self.q[self.front]
        return "Queue is Empty"

    def getRear(self):
        if self.rear != -1:
            return self.q[self.rear]
        return "Queue is Empty"

q = Queue(5)
# print(q.size())
# print(q.empty())
# print(q.getFront())
# print(q.getRear())
print(q.push(5))
print(q.push(1))
print(q.push(4))
print(q.push(3))

# print(q.size())
# print(q.empty())
# print(q.getFront())
# print(q.getRear())

print(q.pop())

print(q.size())
print(q.empty())
print(q.getFront())
print(q.getRear())