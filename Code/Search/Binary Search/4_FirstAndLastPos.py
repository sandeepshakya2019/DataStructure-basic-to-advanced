def FirstPosInSortedArray(arr, target):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = start + int((end - start) / 2)
        if(arr[mid] >= target):
            end = mid - 1
        else:
            start = mid + 1

    if start > len(arr) - 1 : return -1
    if arr[start] == target:
        return start
    else: return -1

def LastPosInSortedArray(arr, target):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = start + int((end - start) / 2)
        if(arr[mid] <= target):
            start = mid + 1
        else:
            end = mid - 1
    if end > len(arr) - 1 : return -1

    if arr[end] == target:
        return end
    else: return -1

# arr = [5,7,7,8,8,10]
# target= 8


arr = [1]
target= 1

print(FirstPosInSortedArray(arr, target))
print(LastPosInSortedArray(arr, target))
