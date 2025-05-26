def binary_search(arr, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return start

def InsertionSort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        # Find the insertion index using binary search in arr[0...i-1]
        idx = binary_search(arr, val, 0, i - 1)
        # Shift elements to the right to make space
        j = i
        while j > idx:
            arr[j] = arr[j - 1]
            j -= 1

        arr[idx] = val
    return arr


arr = [3,1,5,4,2]

InsertionSort(arr)
print("Final",arr)