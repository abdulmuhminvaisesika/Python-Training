def fibonacci_using_generotor(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
generator = fibonacci_using_generotor(100)
for i in range(12):
    print(next(generator),end=" ")
    