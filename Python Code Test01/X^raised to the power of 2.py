# =============================================================================
# # -*- coding: utf-8 -*-
# 
# from pylab import *
# 
# x = int(input("Hvor mange tall"))
# xakse = linspace(0, x, x + 1)
# 
# def f(x):
#     return x**2
# 
# y = zeros(x + 1)
# 
# for i in range(0, x + 1):
#     y[i] = f(i)
#     i += 1
#     
# title("Funksjonen x^2")
# plot(xakse, y)
# xlabel("x-verdier")
# ylabel("y-verdier")
# 
# axhline(400)
# axvline(20)
# 
# show()
# 
# print(linspace(0, x, x + 1))
# print(y)
# print(f(i-1))
# =============================================================================
import numpy as np

Numbers = np.array([1, 2, 3, 4, 5])

def g(x):
    return x**2

print(g(Numbers))
