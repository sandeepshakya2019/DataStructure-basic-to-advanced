# class Solution(object):
#     def rotate(self, matrix):
#         n = len(matrix)
#         ans = [[0]*n for _ in range(n)]
#         # print(ans[0][1], matrix[0][1])
#         var = len(matrix) - 1
#         for i in range(len(matrix)):
#             arr = matrix[i]
#             for j in range(len(arr)):
#                 ans[j][var]=matrix[i][j]
#             var -= 1
        
#         for i in range(len(matrix)):
#             arr = matrix[i]
#             for j in range(len(arr)):
#                 matrix[i][j]=ans[i][j]
#         return matrix
                
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                if i != j:
                    [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
        for i in range(n):
            matrix[i].reverse()

        return matrix
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution().rotate(matrix))