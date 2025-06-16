def sortedArray(arr, i, j, n):
    if i > n or j+1 > n:
        return True
    
    if arr[i] < arr[j]: 
        return sortedArray(arr, i + 1, j + 1, n)
    else: return False

arr = [
    0,2
]
print(sortedArray(arr, 0, 1, len(arr)))
    