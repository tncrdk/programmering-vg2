#Variabler
a = 0
b = 1
Sum = 0

N = 5

#Program
for i in range(N):
    Sum = a + b 
    if i % 2 == 0:
        a = Sum
    else:
        b = Sum

print(Sum)
