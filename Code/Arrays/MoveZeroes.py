class Solution(object):
    def moveZeroes(self, arr):
        n = len(arr)
        i = -1
        j = 0
        while(i < n and j < n):
            print(i, j)
            if arr[j] == 0:
                if i == -1:
                    i = j # pahla zero
                j = j + 1
            else:
                if i != -1 and arr[i] == 0:
                    print("swap", i, j)
                    arr[i], arr[j] = arr[j], arr[i]
                    i = i + 1
                j = j + 1
        print(arr)

# nums = [4,2,4,0,0,3,0,5,1,0]
# nums = [0,1,0,3,12]
nums = [0]
# nums = [4,2,4,0,0,3,0,5,1,0]


Solution().moveZeroes(nums)
        