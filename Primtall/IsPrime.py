from math import sqrt
import time
import numpy as np

PrimeTable = [2, 3, 5, 7]

def IsPrimeConsecutive(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    else:
        MaxLimit = int(sqrt(n))
        Index = 2
        KeepGoing = True
        global PrimeTable
        
        while KeepGoing:
            if n % PrimeTable[Index] == 0:
                return False
            Index += 1
            if Index > MaxLimit:
                PrimeTable.append(n)
                return True
            

def IsPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    else:
        MaxLimit = int(sqrt(n))
        Test = 5
        while True:
            if n % Test == 0:
                return False
            if n % (Test + 2) == 0:
                return False
            Test += 6
            if Test > MaxLimit:
                return True
            
            
def Sieve(MaxLimit):
    AllNum = np.array(np.full(MaxLimit + 1, False))
    Primes = [2, 3]
    
    AllNum[5::6] = True
    AllNum[7::6] = True      
    
    p = 6
    
    while p + 1 < MaxLimit:
        if AllNum[p-1]:
            Primes.append(p-1)
            
            for y in range((p-1)**2, len(AllNum), p-1):
                AllNum[y] = False

        if AllNum[p+1]:
            Primes.append(p+1)
            
            for z in range((p+1)**2, len(AllNum), p+1):
                AllNum[z] = False
        
        p += 6
    
    return Primes


def FactoringWithPrimeTable(x, primes: list):
    factors = {}
    limit = sqrt(x)
    
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

def Sieve2(MaxLimit):    
    AllNum = np.array(np.full(MaxLimit + 1, True))
    AllNum[0:1] = False
    primes = []
    p = 2
    
    while p <= MaxLimit:
        if AllNum[p]:
            primes.append(p)
            for i in range(p**2, len(AllNum), p):
                AllNum[i] = False
        
        if p == 2:
            p += 1
        else:
            p += 2
    
    return primes


# =============================================================================
# Functions
# Execution   
# =============================================================================
            
start = time.time()

arr = Sieve(1000000)
#print(FactoringWithPrimeTable(32, arr))

tot_time = time.time() - start
print(f'Total Tid: {tot_time} sek')














