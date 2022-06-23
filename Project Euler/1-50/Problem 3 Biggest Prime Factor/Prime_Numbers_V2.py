# -*- coding: utf-8 -*-

#Biggest Prime Number

primes = []
#N = 600851475143
N = 20
n = N**0.5

#isprime = True
a = 2

while a <= n:
    for i in primes:
        if a % i == 0:
#            isprime = False
            break
    else:
        primes.append(a)
        print(a)
    a += 1

primes.reverse()

for i in primes:
    if N % i == 0:
        break
print("--------------------------------------------")
print(i)
