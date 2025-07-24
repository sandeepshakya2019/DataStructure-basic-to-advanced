arr = [5,8,9,6,5,47,8,5,26,2,6,2,65]

# largestElem  = max(arr)
# largetsIndex = arr.index(largestElem)
# # print(largestElem, largetsIndex)
# maxelem = -float('inf')

# for i in range(len(arr)):
#     if i != largetsIndex:
#         maxelem = max(maxelem, arr[i])

# print(maxelem)

# largest = -float("inf")

# for item in arr:
#     largest = max(largest, item)

# print(item)

arr = [5, 8, 9, 6, 5, 47, 8, 5, 26, 2, 6, 2, 65]

largest = -float("inf")
secondlargest = -float("inf")

for item in arr:
    if item > largest:
        secondlargest = largest
        largest = item
    elif item > secondlargest and item != largest:
        secondlargest = item

print("Largest:", largest)
print("Second Largest:", secondlargest)

