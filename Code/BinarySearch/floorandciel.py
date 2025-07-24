class Solution(object):
    def findFloor(self, nums, target):
        """
        Finds the greatest element less than or equal to the target.
        Returns the value, or None if no such element exists.
        """
        start, end = 0, len(nums) - 1
        floor_val = None
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                # This is a potential floor, store it and look for a greater one
                floor_val = nums[mid]
                start = mid + 1 
            else:
                # The element is too large, look in the left half
                end = mid - 1
        return floor_val

    def findCeil(self, nums, target):
        """
        Finds the smallest element greater than or equal to the target.
        Returns the value, or None if no such element exists.
        """
        start, end = 0, len(nums) - 1
        ceil_val = None
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                # This is a potential ceiling, store it and look for a smaller one
                ceil_val = nums[mid]
                end = mid - 1
            else:
                # The element is too small, look in the right half
                start = mid + 1
        return ceil_val