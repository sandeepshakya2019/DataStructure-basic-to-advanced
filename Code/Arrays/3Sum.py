# class Solution(object):
#     def threeSum(self, nums):
#         ans = set()
#         for i in range(len(nums)):
#             hashset = set()
#             for j in range(i+1, len(nums)):
#                 third = - (nums[i] + nums[j])
#                 if third in hashset:
#                     arr = [nums[i], nums[j], third]
#                     arr.sort()
#                     ans.add(tuple(arr))
#                 hashset.add(nums[j])
#         return list(ans)

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else: k -= 1
        return list(ans)

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

