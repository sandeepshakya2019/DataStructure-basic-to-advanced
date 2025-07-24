class Solution(object):
    def majorityElement(self, nums):
        c1 = 0
        c2 = 0
        e1 = float("inf")
        e2 = float("inf")
        nC = len(nums) // 3
        arr = []
        for item in nums:
            if c1 == 0 and item != e2:
                e1 = item
                c1 = 1
            elif c2 == 0 and item != e1:
                c2 = 1
                e2 = item
            elif e1 == item:
                c1 += 1
            elif e2 == item:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1            

        c1 = 0
        c2 = 0
        for item in nums:
            if item == e1:
                c1 += 1
            elif item == e2:
                c2 += 1

        if c1 > nC:
            arr.append(e1)
        if c2 > nC:
            arr.append(e2)
        

        return arr

            

nums = [2,2,1,3]
print(Solution().majorityElement(nums))
# class Solution(object):
#     def majorityElement(self, nums):
#         hash = {}
#         arr = []
#         neededCount = len(nums) // 3
#         if len(nums) < 1: return nums
#         for item in nums:
#             if item in hash:
#                 hash[item] = hash[item] + 1
#             else:
#                 hash[item] = 1

#             if hash[item] > neededCount:
#                 arr.append(item)

#         return list(set(arr))
    