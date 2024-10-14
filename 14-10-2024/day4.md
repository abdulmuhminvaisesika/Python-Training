# 14-10-2024

## Python Basics and Practice Problems

### 1.Program: Prime or Not

The goal of this program is to determine whether a given number is prime or not. A prime number is a natural number greater than 1 that is divisible only by 1 and itself.

*Logical View:*

1. Input: Accept a number num as input.
2. Check if the number is greater than 1.
     * If the number is greater than 1, iterate over all numbers from 2 to num-1.
     * If any number in that range divides num evenly, then num is not prime. The loop is broken, and we conclude the number is not prime.
     * If no divisors are found in the range, then the number is prime.

3. Special Case: If the number is 1, it is not prime.

4. Output: The result is printed, stating whether the number is prime or not.

*Code:*
``` python 
def prime_or_not(num):
    # First, check if the number is greater than 1
    if num > 1:         
        for i in range(2, num):  
            # Check if num is divisible by any number i in this range
            if (num % i) == 0:
                
                print(num, "not prime")
                # No need to check further; break out of the loop
                break
        else:
            # If loop completes without finding a divisor, num is prime
            print(num, "prime")
    
    # If num is equal to 1, print that 1 is not prime (special case)
    elif num == 1:
        print(num, "not prime")
    else:
        
        print(num, "not prime")


prime_or_not(29)
```

---
 ### Generators in Python


Generators are a special type of iterable in Python that generate values on the fly, allowing for lazy iteration without storing the entire sequence in memory. This makes them memory-efficient for large datasets or data streams.

Defined like normal functions, generators use the yield keyword instead of return. The yield statement pauses the function, saving its state, so it can resume where it left off when the next value is requested.



*Syntax:*
``` python
def generator_function():
    # Code before yield
    yield value1  # This is the first value yielded
    # Code in between
    yield value2  # This is the second value yielded
    # More code if needed
    yield value3  # This is the third value yielded
```
*Basic Features of Generators:*
1. Memory Efficiency
2. Lazy Evaluation
3. State Preservation
4. Single Iteration
5. Infinite Sequences
6. Simpler Syntax



### Program- Prime Numbers Up to a Range Using Generator

The goal is to generate and yield all prime numbers within a specified range using a generator function. This approach allows for efficient memory usage by generating primes on-the-fly.

*Logical View:*
1. Input: Accept two integers, start and end, defining the range.

2. Iterate: Loop through each number in the range from start to end.

3. Check for Primality:

   * For each number, check if it is greater than 1.

   * Loop through possible divisors from 2 up to the number (exclusive).

   * If the number is divisible by any of these divisors, it is not prime, and the loop breaks.

   * If the loop completes without finding a divisor, the number is prime, and it is yielded.

4. Output: Use the generator to retrieve prime numbers one by one.

*Code:*
``` python

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
```

### Program: Fibonacci Sequence Using Generator

The goal is to generate and yield Fibonacci numbers up to a specified limit n using a generator function. This method allows for efficient memory usage by producing Fibonacci numbers on-the-fly.
   



  *Logical View:*
  1. Input: Accept an integer n that specifies the upper limit for Fibonacci numbers.

2. Initialize: Start with the first two Fibonacci numbers, 0 and 1.

3. Generate:

   * Use a while loop to continue generating numbers as long as the current number is less than n.

   * Yield the current number, then update the values of the two previous numbers to generate the next Fibonacci number.

4. Output: Use the generator to retrieve Fibonacci numbers one by one.

*Code:*
``` python 
def fibonacci_using_generotor(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
generator = fibonacci_using_generotor(100)
for i in range(12):
    print(next(generator),end=" ")
```


## Class In Python
A class in Python is a blueprint for creating objects. It allows you to bundle data (attributes) and functionality (methods) together. Classes enable the principles of Object-Oriented Programming (OOP), such as encapsulation, inheritance, and polymorphism, which promote code reuse and organization.

*Basic Features of Classes:*
1. Encapsulation:

   * Classes encapsulate data and methods that operate on that data, promoting modularity and organization in code.
  
2. Attributes and Methods:
    
    * Attributes are variables that belong to the class, and methods are functions defined within the class that can manipulate these attributes.

3. Instantiation:
    * Classes can be instantiated to create objects. Each object can have different attribute values.

4. Inheritance:
    * Classes can inherit attributes and methods from other classes, promoting code reuse and the creation of hierarchical relationships.

5. Polymorphism:
    * Different classes can define methods with the same name, allowing for interchangeable usage of different classes.

6. Class vs Instance Variables:
    * Class variables are shared across all instances of a class, while instance variables are unique to each instance.


*Syntax for Defining a Class:*
``` python
class ClassName:
    # Class attribute
    class_attribute = value

    def __init__(self, instance_variable):
        # Instance attribute
        self.instance_variable = instance_variable

    def method_name(self):
        # Method that operates on instance attributes
        pass
```


### Program: Prime Numbers and Fibonacci Series Using a Class

To provide functionalities for checking prime numbers, generating prime numbers up to a specified range, and generating the Fibonacci series up to a specified number of terms.
*Logical View:*
1. Class Definition: The PrimeNumber class encapsulates methods related to prime numbers and the Fibonacci sequence.
2. Methods:
   * is_prime: A static method that checks if a given number is prime.
   * prime_numbers_upto_range: An instance method that generates all prime numbers within a specified range.
   * fibonocci_series: An instance method that generates the Fibonacci series up to n terms
3. Input and Output:

    * Take an integer input from the user.
    * Use the methods to check primality, get primes in a range, and generate the Fibonacci series.
*Code:*
``` python
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
```
*Example Output:*
``` python
Enter a number: 10
10 is prime: False
Prime numbers up to 10: [2, 3, 5, 7]
Fibonacci series up to 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### __getattr__ and __getattribute__ in Python

1. __getattribute__
* Purpose: This method is called automatically when any attribute of a class instance is accessed. You can override this method to define custom behavior whenever an attribute is accessed.

*Syntax:*
  ``` python
  def __getattribute__(self, name):
    # Custom behavior
    return super().__getattribute__(name)  # Call the default behavior

```
2. __getattr__

Purpose: This method is called when an attribute is accessed that doesn't exist in the instance's namespace. You can use __getattr__ to provide default values or handle missing attributes gracefully.


*Syntax:*
``` python
def __getattr__(self, name):
    # Custom behavior for missing attributes
    return "Attribute not found!"
```


*Example*
``` python 
class MyDynamicClass:
    def __init__(self):
        self.data = 42

    def __getattribute__(self, name):
        print(f"Getting attribute: {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"'{name}' not found, returning default value.")
        return "Default Value"

obj = MyDynamicClass()
print(obj.data)        # Output: Getting attribute: data \n 42
print(obj.other_data)  # Output: 'other_data' not found, returning default value. \n Default Value
```
### Program-Best Time to Buy and Sell Stock II


To determine the maximum profit that can be achieved by buying and selling a stock on multiple occasions, based on a list of stock prices for consecutive days.


*Logical View:*
1. Class Definition: The BuyAndSell class encapsulates methods related to buying and selling stocks.

2. Methods:
   * __init__: Initializes the class with a list of stock prices.
   * find_profit: Calculates the total profit by summing up all positive price differences between consecutive days.
3. Input and Output:
    * Takes a list of stock prices.
    * Returns the total profit from buying and selling based on the price changes.

*Code:*
``` Python 
class BuyAndSell:
    def __init__(self, lst):
        self.lst = lst

    def find_profit(self):
        profit = 0
        for i in range(1, len(self.lst)):
            # Only add to profit when the price increases
            if self.lst[i] > self.lst[i-1]:
                profit += self.lst[i] - self.lst[i-1]
        return profit

# Example usage
lst = [1,2,3,4,5]
is_profit = BuyAndSell(lst)

print(is_profit.find_profit()) 

```


---


