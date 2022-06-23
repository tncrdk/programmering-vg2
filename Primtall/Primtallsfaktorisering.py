import numpy as np
import time
import math as mth

def PrimeFactoring(x):    
    product = x
    AllNum = np.array(np.full(int(x**0.5) + 1, True))
    factors = {}
    
    AllNum[0] = False
    AllNum[1] = False
    
    for i in range(4, len(AllNum), 2):
        AllNum[i] = False
    
    if product % 2 == 0:
        factors[2] = 0
        
        while product % 2 == 0:
            factors[2] += 1
            product /= 2
    
    p = 3
    
    while p <= x**0.5:
        if AllNum[p]:
            
            for i in range(p**2, len(AllNum), p):
                AllNum[i] = False
            
            if product % p == 0:
                factors[p] = 0
                
                while product % p == 0:
                    factors[p] += 1
                    product /= p
            
            if product == 1:
                return factors
            
        p += 2
        
    if product != 1 and product != x:
        factors[int(product)] = 1
    
    elif product == x:
        factors[product] = "primtall"
        # factors[1] = 1
        # factors[product] = 1
    
    return factors

def FactoringWithPrimeTable(x, primes: list):
    factors = {}
    limit = mth.sqrt(x)
    
    for i in primes:
        if x % i == 0:
            factors[i] = 0
            
            while x % i == 0:
                factors[i] += 1
                x /= i
        
        if x == 1:
            return factors
        
        if i >= limit:
            factors[int(x)] = 1
            return factors
    
    return factors


# =============================================================================
# Function
# Execution
# =============================================================================

start = time.time()

print(PrimeFactoring(516231436549652))

tot_time = time.time() - start
print(f'Total Tid: {tot_time} sek')

