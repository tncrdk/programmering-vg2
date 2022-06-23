#Hanois Tower Using Recursion
# n = the number of discs

def Move(fr, to):
    print("Move from " + str(fr) + " to " + str(to))

def Hanoi(n, f, v, t):
    if n == 0:
        pass
    else:
        Hanoi((n-1), f, t, v)
        Move(f, t)
        Hanoi((n-1), v, f, t)

Hanoi(3, "A", "B", "C")

# =============================================================================
# def MoveVia(fr, via, to):
#     Move(fr, via)
#     Move(via, to)
# =============================================================================
