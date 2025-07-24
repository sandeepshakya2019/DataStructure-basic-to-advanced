class Solution(object):
    def lowerBound(self, nums, target):
        n = len(nums)
        start = 0
        end = n - 1
        ans = n
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def upperBound(self, nums, target):
        n = len(nums)
        start = 0
        end = n - 1
        ans = n
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

nums = [1,2,3,3,3,7,8,9,9,9,11] 

print(Solution().lowerBound(nums, 3))
print(Solution().upperBound(nums, 3))
