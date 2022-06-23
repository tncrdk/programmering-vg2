# -*- coding: utf-8 -*-

N1 = 999999
a = 1
dig = int(999999**0.5)

for i in range(1, 101):
    if a % 10 == 0:
        print(N1)
        for x in range(dig, 100, -1):
            if N1 % x == 0:
                y = N1 / x
                if y < 999 and y > 100:
                     print("--------------------")
                     print(x)
                     print(y)
                
        N1 -= 110
        a += 1
    else:
        print(N1)
        for x in range(dig, 100, -1):
            if N1 % x == 0:
                y = N1 / x
                if y < 999 and y > 100:
                    print("--------------------")
                    print(x)
                    print(y)
        N1 -= 1100
        a += 1
