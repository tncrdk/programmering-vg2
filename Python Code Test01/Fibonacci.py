#Variabler
a = 0
b = 1
Sum = 0

N = 10

#Program
for i in range(N + 1):
    Sum = a + b 
    if i % 2 == 0:
        a = Sum
    else:
        b = Sum

print(Sum)
