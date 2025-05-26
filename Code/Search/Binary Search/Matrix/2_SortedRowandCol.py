matrix = [[10,20,30,40],[15,25,35,45],[28,29,37,49],[33,34,38,50]]

def SortedSearch(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    i = rows - 1
    j = 0
    while (i > -1) and (j < cols):
        elem = matrix[i][j]
        if elem == target: return [i,j]
        if elem > target: i = i - 1
        else: j = j + 1
    return [-1,-1]

print(SortedSearch(matrix, 50))