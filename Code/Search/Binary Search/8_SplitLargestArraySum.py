def Check(arr, m, mid):
    i = 0
    k = 1
    n = len(arr)
    sumi = 0
    while(i < n):
        sumi = sumi + arr[i]
            # print(sumi)
        if(sumi > mid):
            k = k + 1
            sumi = arr[i]
            if(k > m):
                return False
        i = i + 1

    if(k > m):
        return False
    return True


def findSplitLargArraySum(arr, m):
    start = max(arr)
    end = sum(arr)
    if(m == len(arr)) : return start
    if(m == 1): return end
    while(start < end):
        mid = start + int((end - start) / 2)
        checkSol = Check(arr, m, mid)
        if(checkSol): end = mid
        else : start = mid + 1
    return start



arr = [7,2,5,10,8]
m = 2

print(findSplitLargArraySum(arr, m))