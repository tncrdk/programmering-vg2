# -*- coding: utf-8 -*-
from pylab import *

#Variables
a = 0
b = 1
N = int(input("Hvor mange tall?"))
Sum = 0

#Counting
print("Fibonacci sekvensen går som følger")
for i in range(0, N):
    print(a)
    x = a + b
    b = a
    a = x
