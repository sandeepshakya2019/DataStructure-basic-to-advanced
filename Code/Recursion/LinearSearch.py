def LinearSearch(arr, i, n, target):
    if i >= n : return False
    if arr[i] == target : return True
    return LinearSearch(arr, i + 1, n , target)

def LinearSearchAll(arr, i, n, target):
    ans = []
    if i >= n : return ans
    if arr[i] == target : ans.append(i)
    nextCall =  LinearSearchAll(arr, i + 1, n , target)
    for j in nextCall:
        ans.append(j)
    return ans


arr = [46,56,89,88,1,564,61,61,3,6,46,46,1,31,6,46,1,64,61,6]
target = 46
print(LinearSearchAll(arr, 0, len(arr), target))