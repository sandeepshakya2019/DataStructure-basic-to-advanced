# str1 = "Sandeep Shakya"

# print(str1.lower())
# print(str1.split())
# print(list(str1))
# print(str1.find("S"))

def Palindrome(str):
    start = 0
    end = len(str) - 1
    while start < end:
        if str[start] != str[end]:
            return False
        start = start + 1
        end = end - 1
    return True

print(Palindrome(str="abcdcbas"))