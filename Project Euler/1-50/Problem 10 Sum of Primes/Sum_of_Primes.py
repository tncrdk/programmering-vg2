# -*- coding: utf-8 -*-
from math import sqrt
import time

#Defining a function which tells if a number is divisible by a certain factor

def is_factor(N, Factor):
    return N % Factor == 0

#Checking if a certain number is prime by utilizing Is_Factor for all primes up to the sqrt. If a number is divisible function ends and returns false
def is_prime(n: int, primes: list):
    limit = sqrt(n)
    for i in primes:
        if i > limit:
            break
        
        if is_factor(n, i):
            return False
    
    return True

def all_Primes(roof):
    primes = []
    Sum = 2
    
    if roof == 1:
        return 2
    
    count = 1
    
    while True:
        count += 2
        if is_prime(count, primes):
            primes.append(count)
            
            if count >= roof:
                return Sum
            
            Sum += count

start = time.time()
print(all_Primes(2000000))
print(time.time() - start)