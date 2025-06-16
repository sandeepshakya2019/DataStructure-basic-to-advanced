def SubsetRec(arr, ans,i, result):
    if i > len(arr) - 1 : 
        result.append(ans[:])
        return
    ans.append(arr[i])
    SubsetRec(arr,ans, i + 1, result)
    ans.pop()
    SubsetRec(arr, ans, i + 1, result)


arr = "abc"
result = []
SubsetRec(arr, [], 0, result)
print(result)