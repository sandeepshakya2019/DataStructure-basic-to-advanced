import math

def MaxAndMin(arr):
    maxx = -math.inf
    minx = math.inf

    for i in range(len(arr)):
        if arr[i] > maxx:
            maxx = arr[i]
        if arr[i] < minx:
            minx = arr[i]
    return [maxx, minx]
arr = [8,9,63,23,56,45,36,13,56,89,56,454,61,54,894,654,5914,0, -56,88888]

print(MaxAndMin(arr))