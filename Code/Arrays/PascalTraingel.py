class Solution(object):
    def particular(self, r,c):
        n = r - 1
        c = c - 1
        # n C r
        res = 1
        i = 0
        for i in range(c):
            res = res * (n - i)
            res = res // (i+1)
        # print(res)
        return res

    def genarteRow(self, row):
        arr = []
        arr.append(1)
        ans = 1
        if row == 1 : return arr
        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            arr.append(ans)
        return arr

    
    def generate(self, numRows):
        pascal = []
        for i in  range(1, numRows + 1):
            ans = self.genarteRow(i)
            pascal.append(ans)
        return pascal
        
print(Solution().genarteRow(5))