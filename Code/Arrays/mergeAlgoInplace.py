class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1, nums2, and the end of the merged array
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Go backward from the end of both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # If there are any remaining elements in nums2, copy them
        # (This handles the case where nums2 has the smallest elements)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 =[2,5,6]
# n = 3
nums1 = [0]
m = 0
nums2 =[1]
n = 1
print(Solution().merge(nums1, m, nums2, n))