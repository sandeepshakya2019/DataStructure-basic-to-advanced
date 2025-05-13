n = int(input())
arr = []
for i in range(n):
    el = int(input())
    arr.append(el)

target = int(input())


def LinearSearch(arr, n, target):
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

print(LinearSearch(arr, n, target))