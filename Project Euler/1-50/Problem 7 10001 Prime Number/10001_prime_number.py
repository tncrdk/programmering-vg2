# -*- coding: utf-8 -*-

N = 10001

primes = []

a = 2
while len(primes) + 1 <= N:
    
    for i in primes:
        if a % i == 0:
            break
    else:
        primes.append(a)
#        print(a)
    a += 1
    
print(a-1)