import numpy as np
import time


def CollatzStart(Max):
    AllNum = np.array(np.full(Max**2, 0))    
    AllNum[1] = 1
    n = 1
    KeepGoing = True
    MaxLen = 1
    while KeepGoing:
        if Collatz(AllNum, n) > MaxLen:
            MaxLen = Collatz(AllNum, n)
        if n >= Max:
             KeepGoing = False
        n += 1
    
    return MaxLen
            
    
def Collatz(Numbers, Input):
    if Numbers[Input] != 0:
        return Numbers[Input]
    
    if Input % 2 == 0:
        Numbers[Input] = Collatz(Numbers, int(Input/2)) + 1
        return Numbers[Input]
    
    else:
        Numbers[Input] = Collatz(Numbers, Input*3 + 1) + 1
        return Numbers[Input]



# =============================================================================
# Functions
# Calling
# =============================================================================

start = time.time()

# AllNum = np.array(np.full(100000000, 0))    
# AllNum[1] = 1

print(CollatzStart(10000))

tot_time = time.time() - start
print(f'Total Tid: {tot_time} sek')

