#Hanois Tower Using Recursion
# n = the number you want to know the factorial of

def Factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return Factorial(n-1)*n

print(Factorial(100))