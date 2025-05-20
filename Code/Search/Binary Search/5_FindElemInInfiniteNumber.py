def FindElemInINfiniteSortedArray(arr, target):
    start = 0
    end = 1

    while(True):
        while(start <= end):
            mid = start + int((end - start) / 2)
            if(arr[mid] == target): return mid
            if arr[mid] > target: end = mid - 1
            else: start = mid + 1
        
        start = end + 1
        end = 2 * end + start
    
        if (arr[start] > target):
            print(start)
            return -1


arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]

print(FindElemInINfiniteSortedArray(arr, 8))
