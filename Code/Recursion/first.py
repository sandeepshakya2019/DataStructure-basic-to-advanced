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

def f(n):
    if n <= 0 : return 0
    if n == 1 : return 1
    return f(n-1) + f(n-2)

print(f(8))