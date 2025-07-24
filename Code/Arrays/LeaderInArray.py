class Solution(object):
    def replaceElements(self, arr):
        ans = []
        ans.append(arr[-1])
        for i in range(len(arr) - 2, -1, -1):
            if ans[-1] > arr[i]:
                
                continue
            else:
                ans.append(arr[i])
        print(ans)

            

        
arr = [17,18,5,4,6,1]
# arr = [10,22,12,3,0,6]

Solution().replaceElements(arr)