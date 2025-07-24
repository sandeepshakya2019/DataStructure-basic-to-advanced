class Solution(object):
    def spiralOrder(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        ans = []

        top = 0
        right = col - 1
        left = 0
        bottom = row - 1

        while (top <= bottom and left <= right):
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            i = top
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            i = right
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                i = bottom
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans




matrix = [[1,2,3]]
print(Solution().spiralOrder(matrix))