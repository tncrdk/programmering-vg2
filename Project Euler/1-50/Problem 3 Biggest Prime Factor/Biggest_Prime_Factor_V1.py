# -*- coding: utf-8 -*-
import numpy

primes = [1, 2]
temp = []

N = 600851475143
#N = 100

a = 3

while a <= (N**0.5):
    for i in primes:
        if a % i != 0:
            temp.append(True)
        else:
            temp.append(False)
        
        if i == 1:
            temp.remove(False)
            
    if False not in temp:
            primes.append(a)
            print(a)
        
    temp.clear()
        
    a += 2

primes.reverse()
    
for i in primes:
    if N % i == 0:
        x = N % i
        break

#print(primes)
print(x)