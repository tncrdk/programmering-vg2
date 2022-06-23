import numpy as np
import time

start = time.time()

N = 2000000
n = 10

def Sieve(MaxLimit):    
    AllNum = np.array(np.full(MaxLimit + 1, True))
    p = 2
    Sum = 0
    
    AllNum[0] = False
    AllNum[1] = False
    
    while p**2 <= MaxLimit:
        if AllNum[p]:
            for i in range(p**2, len(AllNum), p):
                AllNum[i] = False
        p += 1
    
    for x in range(len(AllNum)):
        if AllNum[x]:
            Sum += x 
    
    return Sum

print(Sieve(N))

tot_tid = time.time() - start
print(f"Total tid: {tot_tid}sek")
