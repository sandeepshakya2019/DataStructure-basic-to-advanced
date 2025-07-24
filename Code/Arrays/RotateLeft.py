arr = [1,2,3,4,5,6,7]

k = 3

def reverse(i, j):
    while(i <= j):
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1

reverse(0, len(arr) - k - 1)
reverse(len(arr) - k, len(arr) - 1)
reverse(0, len(arr) - 1)



# while
print(arr)