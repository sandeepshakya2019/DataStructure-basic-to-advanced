arr = [8,9,63,23,56,45,36,13,56,89,56,454,61,54,894,654,5914]
start = 3
end = 10
target = 56

def SearhInRange(arr, start, end, target):
    while start < end and start < len(arr):
        if arr[start] == target:
            return start
        start = start + 1
    return -1

print(SearhInRange(arr, start, end, target))