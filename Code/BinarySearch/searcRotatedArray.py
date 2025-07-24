class Solution(object):
    def search(self, nums, target):
        first = nums[0]
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target : return mid
            if nums[mid] > first:
                # go right
                start = mid + 1
            else:
                end  = mid - 1
        return -1 
        
nums = [1,3]
target = 3

print(Solution().search(nums, target))