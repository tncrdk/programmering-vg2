import numpy as np
import time

def TriangularNum(x):
    return int((x*(x+1)/2))

def PrimeFactoring(x):    
    product = x
    AllNum = np.array(np.full(int(x**0.5) + 1, True))
    factors = {}
    
    AllNum[0] = False
    AllNum[1] = False
    
    p = 2
    
    while p <= x**0.5:
        if AllNum[p]:
            
            for i in range(p**2, len(AllNum), p):
                AllNum[i] = False
            
            if product % p == 0:
                factors[p] = 0
                
                while product % p == 0:
                    factors[p] += 1
                    product /= p
            
        p += 1
        
    if product != 1 and product != x:
        factors[int(product)] = 1
    
    elif product == x:
        factors[product] = 1
    
    return factors


def Combined(NumFac):
    if NumFac < 2:
        return "Error; Too few factors"
    
    n = 1
    while True:
        Facs = 1
        pfactors = PrimeFactoring(TriangularNum(n))
        for i in pfactors.values():
            Facs *= (i + 1)
        
        if Facs >= NumFac:
            return TriangularNum(n)
        
        n += 1


# =============================================================================
# Functions
# 
# Program
# =============================================================================

start = time.time()

print(Combined(500))

totTime = time.time() - start
print(f'Tot Tid: {totTime} sek')