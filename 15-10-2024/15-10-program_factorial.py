def factorial(n):
    fact=1
    if n <= 0:
        return False
    
    for i in range(1,n+1):

        fact=fact * i

    return fact
print(factorial(n=5))







