class Solution(object):
    def permute(self, nums):
        ans = []
        self.mainAns(nums, 0, ans)
        return ans

    def mainAns(self, up, i, ans):
        if len(up) <= i:
            ans.append(up[:])
            return 
        for j in range(i, len(up)):
            [up[j], up[i]] = [up[i], up[j]]
            # print(copy)
            self.mainAns(up, i+1, ans)
            [up[i], up[j]] = [up[j], up[i]]


    # def mainAns(self, up, i, ans):
    #     if len(up) <= i:
    #         ans.append(up[:])
    #         return 
    #     for j in range(i, len(up)):
    #         copy = up[:]
    #         [copy[j], copy[i]] = [copy[i], copy[j]]
    #         # print(copy)
    #         self.mainAns(copy, i+1, ans)

        
print(Solution().permute(nums=[1,2,3]))