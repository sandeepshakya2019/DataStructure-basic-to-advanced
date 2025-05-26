def CyclicSort(arr):
    i = 0
    n = len(arr)
    while i < n:
        correctIdx = arr[i] - 1
        if arr[i] != arr[correctIdx]:
            arr[i], arr[correctIdx] = arr[correctIdx], arr[i]
        else:
            i = i + 1

arr = [3,5,2,1,4]
CyclicSort(arr)
print(arr)