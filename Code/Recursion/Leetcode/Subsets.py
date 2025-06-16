class Solution(object):
    def subsets(self, nums):
        ans = []
        self.mainAns([], nums, 0, ans)
        return ans

    def mainAns(self, p, up, i, ans):
        if len(up) <= i:
            ans.append(p[:])
            return ans
        # take 
        p.append(up[i])
        self.mainAns(p, up, i+1, ans)
        # not take
        p.pop()
        self.mainAns(p, up, i+1, ans)
        # return ans


        
        
nums = [1,2,3]

print(Solution().subsets(nums))
        