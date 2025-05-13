import math

def FindEvenNumber(arr):
    count = 0
    for i in range(len(arr)):
        digit = math.floor(math.log10(arr[i])) + 1
        lastbit = digit&1
        if lastbit == 0:
            count = count + 1
    return count

arr = [12,345,2,6,7896]
print(FindEvenNumber(arr))
