def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    ans = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i = i + 1
        else:
            ans.append(arr2[j])
            j = j + 1
        

    if i < m:
        while(i < m):
            ans.append(arr1[i])
            i = i + 1
    if j < n:
        while(j < n):
            ans.append(arr2[j])
            j = j + 1

    return ans

def MergeSort(arr):
    if len(arr) == 1: return arr

    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return merge(left, right)

print(MergeSort([8,6,5,9,5,3,6,3,6,2,6]))

