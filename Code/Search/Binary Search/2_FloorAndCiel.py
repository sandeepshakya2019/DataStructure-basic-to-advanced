def CielOfSortedArray(arr, target):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = int((start + end)/2)
        if (arr[mid] == target):
            return mid
        if(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return start

def FloorOfSortedArray(arr, target):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = int((start + end)/2)
        if (arr[mid] == target):
            return mid
        if(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return end


arr = [1,3,5,6]
target = 2
print(FloorOfSortedArray(arr, target))
print(arr[CielOfSortedArray(arr, target)])
