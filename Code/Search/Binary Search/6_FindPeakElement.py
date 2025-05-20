def FindPeakElement(arr):
    start = 0
    end = len(arr) - 1

    while(start < end):
        mid = start + int((end - start) / 2)
        if(arr[mid] > arr[mid+1]):
            # decrising part of the array this may be the ans keep this 
            end = mid
        else:
            start = mid + 1

    return start

arr = [2,4,5,7,8,9,10,12]
print([FindPeakElement(arr)])