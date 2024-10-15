# 15-10-2024 
# Python Basics and Practice Problems


### 1.Program-Factorial of a number

To compute the factorial of a given number n. The factorial is the product of all positive integers up to n.

*Logical View:*
* If n is less than or equal to 0, return False since factorial is only defined for positive integers.
* Use a loop to multiply numbers from 1 to n, accumulating the result in fact.
* Return the factorial value.

*Code:*
``` python
def factorial(n):
    fact=1
    if n <= 0:
        return False
    
    for i in range(1,n+1):

        fact=fact * i

    return fact
print(factorial(n=5))
```

### 2. Integer to Roman Conversion

Convert a given integer into its corresponding Roman numeral representation.


*Logical View:*
* Create a Roman Numeral Dictionary: A dictionary maps integers to their Roman numeral symbols in decreasing order.

* Initialize Result String: Start with an empty string result to build the Roman numeral.

* Loop through Roman Numerals: For each Roman numeral value (from largest to smallest):

* Check Fit: Use integer division (n // value) to see how many times the numeral fits into n.
* Append Symbol: Add the symbol to result that many times.
* Update n: Subtract the corresponding value from n.
* Return the Result: Once all values are processed, return the Roman numeral string.

*Code:*
``` python
def integer_to_roman(n):
    
    
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'}

    result = ''
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        
        #calculates how many times the current Roman numeral value (value) fits into n.
        count = n // value
        
        # appends the corresponding Roman numeral symbol (symbol) to the result string.and multplied with count
        result += symbol * count
        

        #updates n for the next iteration.
        n -= value * count

    return result
    
print(integer_to_roman(n=3749))
```

*Example:*
```
3749

MMMDCCXLIX
```



### 3. Reverse Words in a String

To reverse the order of words in a given string while preserving the individual words.


*Logical View:*
* Split the String into Words: Use the split(" ") method to break the input string into a list of words based on spaces.
* Reverse the List of Words: Reverse the list using slicing (words[::-1]), which creates a new list containing the words in reverse order.
* Join the Reversed Words: Use ' '.join(...) to concatenate the reversed list of words back into a single string, with a space between each word.
* Return the Result: The function returns the newly formed string with the words in reverse order.


*Code:*
``` python
def reverse_words_in_string(string1):
    words=string1.split(" ")
    result = ' '.join(words[::-1])
    return result
print(reverse_words_in_string(string1=""))
```

*Example:*
```
Input: "Hello World"
Output: "World Hello"
```




### 4. Rotate Array
To rotate an array to the right by k positions, where k is a non-negative integer.


*Logical View:*
1. Calculate the Length: Determine the length of the input array arr using len(arr).
2. Compute the Shift Difference: Calculate diff as length - k. This value indicates the starting index for slicing the original array to achieve the rotation.
3. Slice and Rearrange:
* Create a new array arr_rotated that consists of two parts:
    * The elements from the index diff to the end of the array (arr[diff:]).
    * The elements from the start of the array to the index diff (arr[:diff]).
* Concatenate these two slices to form the rotated array.
4. Return the Rotated Array: Finally, return the new rotated array.


*Code:*
``` python

def rotate_array(arr,k):
    arr_rotated=[]
    length=len(arr)
    diff=length-k
    arr_rotated[:]=arr[diff:]+arr[:diff]
    return arr_rotated
    
    

print(rotate_array([1, 2, 3, 4, 5], 3))
```
*Example:*
```
Input: [1, 2, 3, 4, 5], k = 3
Output: [3, 4, 5, 1, 2]
```



### 5.Remove Duplicates from Sorted Array II

This code removes duplicates from a sorted array, ensuring that each unique element appears at most twice. The final result is padded with underscores (_) to maintain the original list length.


*Logical View:*
1. Input Check: If the input list is empty, return False.
2. Count Occurrences: Use Counter to count how often each element appears in the list.
3. Set Repetition Rule: Elements can appear at most twice.
4. Build Result:
    * Add elements that appear 2 or more times twice.
   * Add elements that appear only once once.
5. Padding: If the result list is shorter than the original, fill the remaining spaces with underscores (_).
6. Return the Modified List.

*Code:*
``` python
from collections import Counter

def Remove_Duplicates_from_Sorted_Array(num):
    if not num:
        return False  # Return False if the input list is empty
    
    # Use Counter to count occurrences of each element
    counts = Counter(num) 
    minimum_rep = 2  # Minimum repetition count allowed
    result = []  # Initialize an empty list to store the result

    # Get elements that appear exactly twice
    repeated_elements = {key: value for key, value in counts.items() if value == minimum_rep}
    
    
    if repeated_elements:
        for key, value in counts.items():
            if value >= 2:
                result.extend([key] * 2)  # Add the element twice if it appears twice
            elif value ==1:
                result.extend([key])  # Repeat it to appear twice

        if len(result)<len(num):
            while len(result)!=len(num):
                result.extend("_")
    else:
         print(f"it has to repeact atleast {minimum_rep} times.")
        

        
    return result
print(Remove_Duplicates_from_Sorted_Array([0,1,2,3,5,5,5,4,5,4]))
```
*Output:*
```
[0, 1, 2, 3, 5, 5, 4, 4, '_', '_']
```





___







