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
        
    def letterCombinations(self, digits):
        ans = []
        self.mainAns("", digits, 0, ans)
        return ans

    def mainAns(self, p, up, i, ans):
        print(len(up))
        if len(up) < i:
            ans.append(p)
            return ans
        # processed
        digit = up[i]
        letters = self.mapping[int(digit)]
        for letter in letters:
            self.mainAns(p + letter, up, i+1, ans)

print(Solution().letterCombinations(digits=""))

           
        