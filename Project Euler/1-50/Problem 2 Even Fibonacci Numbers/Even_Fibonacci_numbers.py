# -*- coding: utf-8 -*-
import numpy

Sum = 0
a = 0
b = 1
n = b

while Sum <= 4000000:
    if a % 2 == 0:
        Sum += a
    n = b
    b = a + b
    a = n

print(Sum)
