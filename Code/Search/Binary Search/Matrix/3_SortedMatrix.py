matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

def BSonCols(arr, target):
    above = 0
    below = 0
    i = 0
    j = len(arr) - 1
    while(i <= j):
        mid = i + int((j - i)/2)
        print(arr[mid], mid)
        if arr[mid] == target : return [mid, above, below]
        if arr[mid] > target : 
            j = mid - 1
            below = mid + 1
        else : 
            i = mid + 1
            above = mid - 1
        print("above :: ", above)
        print("below :: ", below)

    return [-1, above, below]

def BS(matrix, target, row):
    arr = matrix[row]
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = i + int((j - i)/2)
        # print(arr[mid], mid)
        if arr[mid] == target : return mid
        if arr[mid] > target : j = mid - 1
        else : i = mid + 1
    return -1
    

def SearchSortedMatrix(matrix, target):
    j = 0
    i = 0
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1

    # print(rows, cols)
    midColj = int((j + cols) / 2)
    # print(midColj)
    arr = []
    for k in range(rows + 1):
        arr.append(matrix[k][midColj])
    find = BSonCols(arr, target)
    if (find[0] != -1): return [find[0], midColj]
    noOfRows = find[2] - find[1]
    # print(find)

    if(noOfRows == 1):
        f = BS(matrix, target, find[1])
        if(f != -1): return [find[1], f]
    elif(find[2] == 0):
        f = BS(matrix, target, find[1] + 1)
        if(f != -1): return [find[1] + 1, f]
    else : 
        for i in range(find[1] + 1, find[2]):
            print(i)
            f = BS(matrix, target, i)
            if(f != -1): return [i, f]
    return [-1, -1]
        

    

print(SearchSortedMatrix(matrix, 5))