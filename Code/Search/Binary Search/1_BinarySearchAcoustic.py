def BinarySearchAscending(arr, target):
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
    return -1


def BinarySearchDescending(arr,target):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        # mid = int((start + end)/2)
        mid = start + int((end - start) / 2)
        if(arr[mid] == target):
            return mid
        if(arr[mid] > target):
            start = mid + 1
        else:
            end = mid - 1
    return -1

def BinarySearchAcoustic(arr, target):
    if(len(arr) < 1):
        if(arr[0] == target): return 0;
        else: return -1
    
    if(arr[0] > arr[len(arr) - 1]):
        return BinarySearchDescending(arr, target)
    else:
        return BinarySearchAscending(arr, target)
    
arr = [2,4,6,9,11,12,14,20,36,48]
target  = 4
print(BinarySearchAcoustic(arr, target))