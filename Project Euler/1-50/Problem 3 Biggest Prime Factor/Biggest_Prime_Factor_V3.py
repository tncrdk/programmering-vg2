# -*- coding: utf-8 -*-
from math import sqrt
import time

start = time.time()
#Biggest Prime Factor V3
factors = []
primes = []

# N = 600851475143
N = 2000001
a = 2

while len(primes) + 1 <= N:
    for i in primes:
        if a % i == 0:
            break
    else:
        primes.append(a)
        
        if N % a == 0:
            factors.append(a)
            N = N / a
    
    a += 1

factors.sort()
print(factors[-1])
tot_time = time.time() - start
print(f'Total Tid: {tot_time} sek')