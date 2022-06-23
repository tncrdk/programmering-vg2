# -*- coding: utf-8 -*-

#a og b er faktorene som blir sjekket for. N er for hvor mange tall
def functionBang(a, b, N):
    
    for i in range(1, N + 1):
        x = i % a
        y = i % b
        
        if x == 0 and y == 0:
            print("Knall!")
        
        elif x == 0:
            print("Bang!")
            
        elif y == 0:
            print("Pang!")
            
        else:
            print(i)

functionBang(10, 3, 100)
