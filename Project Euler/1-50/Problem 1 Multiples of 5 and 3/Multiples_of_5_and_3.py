N = 1000

a = 5
b = 3

Sum = 0

for i in range(1, N):
    if i % a == 0:
        Sum += i
    elif i % b == 0:
        Sum +=i
    else:
        pass

print(Sum)
