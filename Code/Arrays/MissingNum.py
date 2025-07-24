# Input: nums = [3,0,1]

# Output: 2
nums = [0,1]

class Solution(object):
    def missingNumber(self, arr):
        n = len(arr)
        i = 0
        while i < n:
            correctIndex = arr[i]
            if correctIndex < n and correctIndex != i:
                arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
            else:
                i = i + 1
        for i in range(n):
            if arr[i] != i:
                print(i)
                return i
        print(i + 1)
        return i + 1

Solution().missingNumber(nums)