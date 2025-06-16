# Facotrial
# fibonaaci
# power finding
# print countinh


def fact(n):
    if n == 0 or n == 1 :
        return 1
    
    return n * fact(n - 1)

def fib(n):
    if n == 0 or n == 1 :
        return n
    
    return fib(n - 1) + fib(n - 2)


def ultaocunt(n):
    if n < 0 :
        return 0
    print(n)
    ultaocunt(n-1)

def seedhaCount(n):
    if n < 0:
        return 0
    seedhaCount(n-1)
    print(n)

def power(a , b):
    if b == 0:
        return 1
    
    if b == 1:
        return a
    
    half = power(a, b // 2)

    if (b % 2) == 0:
        return half * half
    
    else:
        return  half * half * a
    
print(power(2, 5))