def Collatz(Input):
    if Input == 1:
        return 1
    elif Input % 2 == 0:
        return Collatz(Input/2) + 1
    else:
        return Collatz(Input*3 + 1) + 1


def BigSeq(Max):
    MaxLen = 0
    for i in range(Max - 1, 0, -1):
        N = Collatz(i)
        if N > MaxLen:
            MaxLen = N
            print(i)
    
    return MaxLen
    
print(BigSeq(101))