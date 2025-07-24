class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while(k < l):
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    if sum < target:
                        k += 1
                    else:
                        l -= 1
        return list(ans)
    
# class Solution(object):
#     def fourSum(self, nums, target):
#         nums.sort()
#         ans = []
#         n = len(nums)
        
#         for i in range(n):
#             # OPTIMIZATION 1: Skip duplicate 'i' values
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
            
#             for j in range(i + 1, n):
#                 # OPTIMIZATION 2: Skip duplicate 'j' values
#                 if j > i + 1 and nums[j] == nums[j-1]:
#                     continue
                
#                 # Use two pointers for the remaining part
#                 k = j + 1
#                 l = n - 1
                
#                 while k < l:
#                     current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    
#                     if current_sum < target:
#                         k += 1
#                     elif current_sum > target:
#                         l -= 1
#                     else:
#                         # Found a quadruplet
#                         ans.append([nums[i], nums[j], nums[k], nums[l]])
#                         k += 1
#                         l -= 1
                        
#                         # OPTIMIZATION 3: Skip duplicates for 'k' and 'l'
#                         while k < l and nums[k] == nums[k-1]:
#                             k += 1
#                         while k < l and nums[l] == nums[l+1]:
#                             l -= 1
                            
#         return ans
        

nums =[1,0,-1,0,-2,2]
target = 0
print(Solution().fourSum(nums, target))