matrix = [[1,1,1],[1,0,1],[1,1,1]]
class Solution(object):
    def makeRowZero(self, r, matrix):
        for col in range(len(matrix[r])):
            matrix[r][col] = 0
        
    def makeColZero(self, c, matrix):
        for row in range(len(matrix)):
            matrix[row][c] = 0


    def setZeroes(self, matrix):
        row = [0 for _ in matrix]
        col = [0 for _ in matrix[0]]
        for i in range(len(matrix)):
            arr = matrix[i]
            for j in range(len(arr)):
                elem = arr[j]
                if elem == 0:
                    row[i] = 1
                    col[j] = 1
        # print(row)
        # print(col)

        for i in range(len(row)):
            if row[i] == 1:
                self.makeRowZero(i, matrix)
        
        for i in range(len(col)):
            if col[i] == 1:
                self.makeColZero(i, matrix)
            
        print(matrix)


        
Solution().setZeroes(matrix)