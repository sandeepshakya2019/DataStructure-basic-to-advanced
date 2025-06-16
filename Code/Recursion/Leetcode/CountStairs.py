class Solution(object):
    def climbStairs(self, n):
        return self.mainAns(n)
    
    def mainAns(self, end):
        if end == 0:
            return 1
        
        if end < 0:
            return 0
        
        # go 1 step
        a1 = self.mainAns(end - 1)
        a2 = self.mainAns(end - 2)

        return a1 + a2

print(Solution().climbStairs(3))

class Solution(object):
    def __init__(self):
        self.done = []

    def climbStairs(self, n):
        self.done = [0 for i in range(n + 1)]

        return self.mainAns(n)
        
    
    def mainAns(self, end):
        if end < 0:
            return 0
        if end == 0:
            return 1
        if self.done[end] != 0:
            return self.done[end]

        # Recursive calculation with memoization
        self.done[end] = self.mainAns(end - 1) + self.mainAns(end - 2)
        return self.done[end]


        # return  self.done[end]

print(Solution().climbStairs(3))