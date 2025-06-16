class Solution:
    def __init__(self):
        self.count = 0

    def findAns(self, sumi):
        self.mainAns(0, sumi)
        print(self.count)

    def mainAns(self, pans, upans):
        for i in range(1, 7):  
            getSum = pans + i
            leftSum = upans - getSum

            if leftSum == 0:
                self.count += 1
            elif leftSum > 0:
                self.mainAns(getSum, upans)  



a = Solution()
a.findAns(4)

            