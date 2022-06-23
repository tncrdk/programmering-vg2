# -*- coding: utf-8 -*-

N = 100

primes = []

a = 2

factors = []

x = 0

while a <= N:
    for i in primes:
        if a % i == 0:
            break
    else:
        primes.append(a)
        
        count = 1
        
        while (a**count) <= N:
            x = a**(count)
            count += 1
        factors.append(x)
                  
    a += 1
product = 1
for i in factors:
    product = i*product

print(product)
#print(primes)