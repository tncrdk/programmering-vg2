# -*- coding: utf-8 -*-

NewList = [5, 4, 3, 2, -1, -2]
total = 0

for i in NewList:
    print(NewList[i])
    if i <= 0:
        total += NewList[i]
print()
print(total)
print()

total2 = 0

for i in range(len(NewList)):
    if NewList[i] <= 0:
        total2 += NewList[i]
print(total2)
