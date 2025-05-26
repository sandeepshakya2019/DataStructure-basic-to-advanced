def SquarePattern(n, m):
    rows = n
    cols = m

    for i in range(n):
        for j  in range(m):
            print("*" , end=" ")
        print()


def SomePattern(n, m):
    rows = n
    cols = m

    for i in range(n):
        for j  in range(i, m):
            print("*" , end=" ")
        print()

def SomePattern(n, m):
    for i in range(n):
        for j  in range(0, i):
            print("*" , end=" ")
        print()


SomePattern(5,5)