class Solution(object):
    def __init__(self):
        self.mapping = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        self.ans = []
        self.strings = []

    def letterCombinations(self, digits):
        self.mainAns("", digits, 0, 0)
        for s in self.ans:
            if len(s) == len(digits):
                self.strings.append(s)
        return self.strings
           
        

    def mainAns(self, p, up, i, j):
        if len(up) <= i:
            return 
        digitVal = self.mapping[int(up[i])]
        i = i + 1
        for l in digitVal:
            # print(p, up, i , j, l, p+ l)
            self.mainAns(p + l, up, i, j)
            self.ans.append(p + l)
        # print(self.ans)


        

sol = Solution().letterCombinations("23")
print(sol)