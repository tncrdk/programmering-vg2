import time
import math as mth
import numpy as np

start = time.time()

def PrimeTable(MaxLimit):
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


def Factoring(x, primes: list):
    factors = 1
    limit = mth.sqrt(x)
    
    for i in primes:
        if x % i == 0:
            NumPrime = 1
            
            while x % i == 0:
                NumPrime += 1
                x /= i
            
            factors *= NumPrime
        
        if x == 1:
            return factors
        
        if i >= limit:
            factors *= 2
            return factors
    
    return factors

        
def NFactors(Number_Of_Factors):
    primes = PrimeTable(6000)
    
    nth_number = 1
    first_term_factors = 1
    
    while True:
        if nth_number % 2 == 0:
            second_term_factors = Factoring(nth_number+1, primes)
            NumFac = first_term_factors * second_term_factors
        
        else:
            second_term_factors = Factoring((nth_number+1)/2, primes)
            NumFac = first_term_factors * second_term_factors
        
        if NumFac >= Number_Of_Factors:
            return nth_number*(nth_number+1)/2, nth_number, NumFac
        
        nth_number += 1
        first_term_factors = second_term_factors
        

# =============================================================================
# Functions
# Execution
# =============================================================================

print(NFactors(500))

tot_time = time.time() - start
print(f'Total Tid: {tot_time} sek')




