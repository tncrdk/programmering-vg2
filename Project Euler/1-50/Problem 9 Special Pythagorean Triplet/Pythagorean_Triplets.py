# -*- coding: utf-8 -*-
from math import sqrt

def Pyt(N, a):
    while a < int((N-3)//3):
        for b in range(a+1, (N-2)//2):
            c = sqrt(a**2 + b**2)
# =============================================================================
#             if a + b + c == N:
#                 print(f'{a} + {b} + {c}')
#                 print(a * b * c)
#                 return
# =============================================================================
            if N % (a + b + c) == 0:
                rel = N / (a + b + c)
                a *= rel
                b *= rel
                c *= rel
                print(f'{a} + {b} + {c}')
                print(a * b * c)
                return
        a += 1

Pyt(1000, 1)
