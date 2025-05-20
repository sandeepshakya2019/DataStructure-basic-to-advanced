def FindLowerElem(arr):
    firstElem = arr[0]
    start = 0
    end = len(arr) - 1

    while(start < end):
        mid = start + int((end - start) / 2)
        if(arr[mid] >= firstElem):
            start = mid + 1
        else:
            end = mid
        
    return start

def RangeBS(arr, target, start, end):
    while start <= end:
         mid = start + int((end - start) / 2)
         if(arr[mid] == target): return mid
         if(arr[mid] > target):
            end = mid - 1
         else:
            start = mid + 1
    return -1

def Search(arr, target):
    lowerIndex = FindLowerElem(arr)
    print(lowerIndex)
    findFirstHalf = RangeBS(arr, target, 0, lowerIndex - 1)
    if(findFirstHalf == -1):
        findSecondHalf = RangeBS(arr,target ,lowerIndex, len(arr) - 1)
        return findSecondHalf
    else:
        return findFirstHalf



arr = [2,9,2,2,2]
print(Search(arr, 1))