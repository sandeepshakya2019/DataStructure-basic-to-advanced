class Solution(object):
    def first(self, nums, target):
        n = len(nums)
        start = 0
        end = n - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target : ans = mid
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def last(self, nums, target):
        n = len(nums)
        start = 0
        end = n - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target : ans = mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def searchRange(self, nums, target):
       arr = [self.first(nums, target), self.last(nums, target)]
       return arr
    
nums = [5,7,7,8,8,10]
target = 8

print(Solution().searchRange(nums, target))
