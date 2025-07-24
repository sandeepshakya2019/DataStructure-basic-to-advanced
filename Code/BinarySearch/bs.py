# class Solution(object):
#     def search(self, nums, target):
#         n = len(nums)
#         start = 0
#         end = n - 1
#         while start <= end:
#             mid = (start + end) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[mid] < target:
#                 # go to right side
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return -1

class Solution(object):
    def search(self, nums, target):
        return self.bs(nums, target, start=0, end = len(nums) - 1)
    
    def bs(self, nums, target, start, end):
        if start > end : return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.bs(nums, target, mid + 1, end)
        else: return self.bs(nums, target, start, mid - 1)
    
nums = [-1,0,3,5,9,12] 
target = 9

print(Solution().search(nums, target))