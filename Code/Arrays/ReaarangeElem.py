# class Solution(object):
#     def rearrangeArray(self, nums):
#         positive = []
#         negative = []

#         for num in nums:
#             if num >= 0:
#                 positive.append(num)
#             else:
#                 negative.append(num)
#         print(len(positive))
#         print(len(negative))

#         i = 0
#         j = 0
#         k = 0
#         while j < len(positive) and k < len(negative):
#             print(i, j , k)
#             nums[i] = positive[j]
#             i = i + 1
#             nums[i] = negative[k]
#             i = i + 1

#             j = j + 1
#             k = k + 1
#         print(nums)
#         return nums

class Solution(object):
    def rearrangeArray(self, nums):
        i = 0 # keep track of poisitve
        j = 1 # keep track of negative
        k = 0
        ans = [_ for _ in range(len(nums))]
        while k < len(nums):
            if nums[k] >= 0:
                ans[i] = nums[k]
                i += 2
            else:
                ans[j] = nums[k]
                j += 2
            k += 1
        print(ans)
nums = [-3,1,-2,6]
Solution().rearrangeArray(nums)