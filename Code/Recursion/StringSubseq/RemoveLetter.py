def removeLetter(stri, i, ans, target):
    if i > len(stri) - 1 : return ans
    if stri[i] != target : ans += (stri[i])
    return removeLetter(stri, i + 1, ans, target)

stri = "baccad"
print(removeLetter(stri, 0, "", "a"))