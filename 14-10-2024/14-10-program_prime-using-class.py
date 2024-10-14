class PrimeNumber:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def prime_numbers_upto_range(self, start, end):
        prime_numbers = []
        for num in range(start, end + 1):
            if PrimeNumber.is_prime(num):  # Call the static method
                prime_numbers.append(num)
        return prime_numbers
    
    def fibonocci_series(self, n):
        a, b = 0, 1
        series = []
        for _ in range(n):
            series.append(a)
            a, b = b, a + b
        return series

n=int(input("Enter a number: "))
# Create an instance of the PrimeNumber class
prime_obj = PrimeNumber(n)

# Check if the number 17 is prime
print(prime_obj.is_prime(prime_obj.number))  # Output: True

# Get prime numbers in the range from 1 to 10
print(prime_obj.prime_numbers_upto_range(1, n))  # Output: [2, 3, 5, 7]

print(prime_obj.fibonocci_series(n))
