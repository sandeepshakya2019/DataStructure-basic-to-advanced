from collections import deque

queue = deque()

# Push elements (enqueue)
queue.append(10)
queue.append(20)
queue.append(30)

# Front and Rear
print("Front:", queue[0])   # 10
print("Rear:", queue[-1])   # 30

# Pop element (dequeue)
print("Popped:", queue.popleft())  # 10

# Size
print("Size:", len(queue))  # 2

# Check if empty
print("Is Empty:", len(queue) == 0)  # False
