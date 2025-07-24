arr1 = [1,1,2,2,3,4,5]
arr2 = [2,3,4,4,5]

i = 0
j = 0

u = []

while(i < len(arr1) and j < len(arr2)):
    if arr1[i] > arr2[j]:
        if len(u) == 0 or u[-1] != arr2[j]:
            u.append(arr2[j])
        j = j + 1
    else:
        if len(u) == 0 or u[-1] != arr1[i]:
            u.append(arr1[i])
        i = i + 1
print(u)

