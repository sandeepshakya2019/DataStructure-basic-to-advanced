def BinarySearch(arr, start, end, target):
    if start == end:
        if (arr[start] == target): return start
        else : return -1
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearch(arr, start, mid - 1, target)
    else: return BinarySearch(arr, mid + 1, end, target)

arr = [2, 4, 6, 8, 10, 12, 14, 16]

print(BinarySearch(arr, 0, len(arr) - 1, 16))