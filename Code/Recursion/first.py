# stri = "Hello World"

# def printRec(string, i, n):
#     if (i > n - 1):
#         return;
#     print(string)
#     printRec(string, i+1, n)

# printRec(stri, 0, 5)

# def printNumberSeedha(n):
#     if (n > 5): return
#     printNumberSeedha(n+1)
#     print(n)

# printNumberSeedha(1)

# def f(n):
#     if n <= 0 : return 0
#     if n == 1 : return 1
#     return f(n-1) + f(n-2)

# print(f(8))

# print(98 // 10)

# def SUmOfDigit(num):
#     if num <= 0 : return 0
#     lastdigit = num % 10
#     num = num // 10
#     return lastdigit + SUmOfDigit(num)

# print(SUmOfDigit(2312724))

# def ReverseANum(num):
#     revNm = 0
#     while num > 0:
#         revNm = revNm * 10 + (num % 10)
#         num = num // 10
#     print(revNm)

# ReverseANum(568)

# def ReverseHelper(num, rev):
#     if num == 0:
#         return rev
#     return ReverseHelper(num // 10, rev * 10 + num % 10)

# print(ReverseHelper(568, 0))

# def ReverString(str, revstr, i):

# print(ReverString("sadneep", "", 0))