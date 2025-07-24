# def permutations(p, up, i):
#     if len(up) <= i:
#         p.append(up[:])
#         return 
#     for j in range(i, len(up)):
#         [up[i], up[j]] = [up[j], up[i]]
#         permutations(p, up, i+1)
#         [up[j], up[i]] = [up[i], up[j]]


# p = []
# permutations(p, up, 0)
# print(p)

class Solution(object):
    def nextPermutation(self, nums):
        

        
        
up = [3,2,1]
Solution().nextPermutation(up)