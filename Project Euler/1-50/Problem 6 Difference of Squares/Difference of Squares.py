# -*- coding: utf-8 -*-

N = 100
Sum = 0
Squares = 0

for i in range(1, N + 1):
    Sum += i
Sum = Sum**2

for x in range(1, N + 1):
    Squares += (x**2)
    
print(Sum - Squares)
