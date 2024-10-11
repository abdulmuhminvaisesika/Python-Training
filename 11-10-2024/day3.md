# 11 - 10 - 2024 Python Training and Practice Problem


## Decorators in Python
A decorator in Python is a function that allows you to modify the behavior of another function or method. Decorators enable adding functionality to existing functions or methods in a clean, readable, and reusable manner.

### Syntax:

```python 
@decorator_name
def function_name():
    # function body
```
### Example of a Basic Decorator
```python
def my_decorator(func):
    """
    A simple decorator that wraps the function
    with additional functionality.
    """
    def wrapper():
        print("Something before the function runs")
        func()  # Calling the original function
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    """A simple function that prints 'Hello!'"""
    print("Hello!")

# Calling the decorated function
say_hello()
```
### output:
```bash
Something before the function runs
Hello!
Something after the function runs

```

### Why Use Decorators:
* Code Reusability: Decorators allow you to define reusable wrappers for functions, so you don't have to repeat code across multiple functions.
* Separation of Concerns: You can separate core logic from cross-cutting concerns like logging or error handling.
* Enhanced Readability: Applying a decorator to a function using the @decorator_name syntax makes the code cleaner and more readable.
  

### Types Of Decorators:

**1. @staticmethod**

The @staticmethod decorator is used to define methods inside a class that don't need access to the instance (self) or the class (cls). They behave like regular functions but reside in the class' namespace.

Example Code:
```python 
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Calling the static method without creating an instance
print(MathOperations.add(5, 3))  # Output: 8

```

**2. @classmethod**

The @classmethod decorator is used to define methods that work on the class level. The method receives the class (cls) as its first argument. These methods can modify class attributes and are often used for alternative constructors.

Example Code:

```python
class Animal:
    species = "Mammal"

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species

# Modifying the class attribute using a class method
Animal.set_species("Reptile")
print(Animal.species)  # Output: Reptile
```

**3. @property**

The @property decorator is used to define a method as a property, which allows you to access it like an attribute. This is often used for getter methods, and @property can be paired with @setter to modify the behavior when setting a value.

Example Code:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.1416 * (self._radius ** 2)

c = Circle(5)
print(c.area)  # Output: 78.54

```
**4. @functools.lru_cache**

The @functools.lru_cache decorator is used to cache the results of a function, making it more efficient for repeated calls with the same arguments. It stores the results in a cache and avoids recomputation for previously computed inputs.


Example Code:

```python
from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55
```

**5. @wraps (from functools)**

The @wraps decorator is used to preserve the metadata (like the docstring and function name) of the original function when wrapped by another decorator. Without @wraps, the metadata of the original function would be lost when wrapped by a decorator.

Example Code:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greets a person by name."""
    print(f"Hello, {name}")

greet("Alice")
print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Greets a person by name.

```


> Note: *These five decorators cover a wide range of functionality, from class-level methods to caching and preserving function metadata, and are commonly used in Python development.*



___
## `.get()` Method for Dictionaries:

The dict.get() method in Python is a safe way to retrieve the value of a key from a dictionary. Unlike accessing the key directly using square brackets ([]), get() allows you to specify a default value to return if the key is not found in the dictionary. If no default value is provided, it returns None.

### Syntax:
```python 
dict.get(key, default=None)
```
### Parameters:
* key (required):
The key for which the value is to be retrieved from the dictionary.
* default (optional):
The value to return if the key is not found in the dictionary. If not provided, the method defaults to None.

### Example Code:

``` python 
my_dict = {'name': 'Alice', 'age': 25}

# Retrieving an Existing Key
print(my_dict.get('name'))  # Output: Alice

# Using a Default Value if Key is Absent
print(my_dict.get('gender', 'Not specified'))  # Output: Not specified

# Returning None When the Key is Not Found
print(my_dict.get('address'))  # Output: None
```

---
## Comprehensions in Python

Comprehensions in Python are concise syntactic constructs that allow for the creation of collections such as lists, sets, or dictionaries in a clear and efficient manner. Comprehensions help make the code more readable and can often result in fewer lines of code compared to traditional loops.
### Types of Comprehensions
**1.List Comprehension**

 A list comprehension creates a new list by applying an expression to each item in an iterable, optionally filtering items with a conditional statement.

*Syntax:*
```python
new_list = [expression for item in iterable if condition]
```
*Example:*
```python 
# Create a list of squares for even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]
```
**2.Set Comprehension**

A set comprehension creates a new set in a similar way to list comprehensions, ensuring that all items are unique.

*Syntax:*
```python
new_set = {expression for item in iterable if condition}
```
*Example*
```python
# Create a set of unique vowels from a string
unique_vowels = {char for char in 'abracadabra' if char in 'aeiou'}
print(unique_vowels)  # Output: {'a'}
```

**3.Dictionary Comprehension**

A dictionary comprehension creates a new dictionary from an iterable, where each item is transformed into a key-value pair.

*Syntax:*
```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```
*Example*
```python
# Create a dictionary mapping numbers to their squares
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
**4.Generator Comprehension**

A generator comprehension is similar to list comprehensions but produces a generator object instead of a list. This is useful for large datasets where you want to save memory.

*Syntax:*
``` python
new_generator = (expression for item in iterable if condition)
```

*Example:*
``` python
# Create a generator for squares of even numbers
squares_gen = (x**2 for x in range(10) if x % 2 == 0)
print(list(squares_gen))  # Output: [0, 4, 16, 36, 64]
```

___
## Python Program Solving
### 1.Finding the Majority Element in an Array

The goal of this program is to identify the majority element(s) in a given array. A majority element is defined as an element that appears more than half the time in the array. The program will count the frequency of each element and return the element(s) that occur most frequently.

*Logical View:*

1.Frequency Count: The program utilizes a dictionary to count how many times each element appears in the array.

2.Determine Maximum Frequency: After counting, the program identifies the maximum frequency from the counts.

3.Collect Majority Elements: Finally, it collects all elements that have the maximum frequency and returns them as the result.

*Code:*
``` python
def find_most_frequent_elements(arr):
    count = {}
    
    # Count the frequency of each element
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # Find the maximum frequency
    max_frequency = max(count.values())
    
    # Find all elements that have the maximum frequency
    most_frequent_elements = [key for key, value in count.items() if value == max_frequency]
    
    return most_frequent_elements

# Example usage:
a = [1, 2, 2, 1, 1, 1, 1]
output = find_most_frequent_elements(a)
print(output)  # Output: [1]
```

### 2.Best Time to Buy and Sell Stock

The goal of this program is to determine the best days to buy and sell stock based on a list of prices representing stock prices over a series of days. The program calculates the maximum profit possible by iterating through all combinations of buy and sell days.


*Logical View:*

1. Initialization: The program starts by initializing variables to track the maximum profit, the day to buy, and the day to sell

2. Iterate Through Prices: The program uses nested loops to consider all pairs of days (buy and sell) to calculate potential profits.

3. Profit Calculation: For each pair of days, the profit is calculated as the difference between the selling price and the buying price.

4. Track Maximum Profit: If a new maximum profit is found, the program updates the maximum profit along with the corresponding buy and sell days.

5. Output Results: Finally, the program outputs the maximum profit along with the specific days to buy and sell. If no profit is possible, it indicates that as well.


*code:*
``` python
input_days = [7, 9, 6, 4, 3, 1]

max_profit = 0      # Initialize maximum profit
buy_day = 0         # Day to buy
sell_day = 0        # Day to sell

# Iterate through all combinations of buy and sell
for i in range(len(input_days)):
    for j in range(i + 1, len(input_days)):
        buy_price = input_days[i]
        sell_price = input_days[j]
        
        # Calculate profit
        profit = sell_price - buy_price
        
        # Check if this profit is the best we have found
        if profit > max_profit:
            max_profit = profit
            buy_day = i          # Day to buy (index)
            sell_day = j         # Day to sell (index)

# Output results
if max_profit > 0:
    print(f"Maximum Profit: {max_profit}")
    print(f"Buy on Day: {buy_day + 1} (Price: {input_days[buy_day]})")
    print(f"Sell on Day: {sell_day + 1} (Price: {input_days[sell_day]})")
else:
    print("No profit possible.")
```



### 3.Valid Palindrome Checker


The goal of this program is to determine whether a given input string is a valid palindrome. A palindrome is a string that reads the same forwards and backwards, ignoring spaces, punctuation, and case differences. This program cleans the input string by removing non-alphanumeric characters and then checks if the cleaned string is a palindrome.

*Logical View:*
1. Input String: The program begins with an input string that may contain various characters, including letters, numbers, punctuation, and spaces.
2. Cleaning the String: The program filters out non-alphanumeric characters and converts all characters to lowercase to create a cleaned string.
3. Palindrome Check: It then checks if the cleaned string is equal to its reverse.
4. Output Result: Finally, the program outputs whether the input string is a palindrome or not based on the check.


*Code:*
``` python
# Example input string
input_string = "10, %malayalam, 01 "

# Clean the string by keeping only alphanumeric characters and converting to lowercase
cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

# Check if the cleaned string is equal to its reverse
is_palindrome = cleaned_string == cleaned_string[::-1]

# Output the result
if is_palindrome:
    print("palindrome.")
else:
    print("not a palindrome.")
```







