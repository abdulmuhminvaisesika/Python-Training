def prime_generator(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
genarate=prime_generator(1, 100)
print(next(genarate))