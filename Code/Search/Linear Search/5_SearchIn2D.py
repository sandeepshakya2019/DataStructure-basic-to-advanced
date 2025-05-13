def SearchIn2D(arr, target):
    for i in range(len(arr)):
        ar = arr[i]
        for j in range(len(ar)):
            if arr[i][j] == target:
                return [i,j]
    return [-1,-1]

arr = [[2,3,4], [5,6,3], [1,9], [10]]

print(SearchIn2D(arr, 9))