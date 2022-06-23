liste = [8, 5, 3, 2, 2, 1, -1, -3, -4, -6, -7, -8, -8, -9]

total1 = 0

i = len(liste) - 1

while liste[i] <= 0:
    total1 += liste[i]
    i -= 1

print(total1)
