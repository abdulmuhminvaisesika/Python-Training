# Practice Python Programs

### 1. Sorting a List (without using built-in `sorted` function)

To sort a list without using the built-in `sorted` function, we can implement the Bubble Sort algorithm. This algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 

### Code:

```python
unsorted_list = [2, 10, 3, 4, 5, 7, 1, 8]

for i in range(len(unsorted_list)):  # Loop runs for each element in the list
    for j in range(0, len(unsorted_list) - i - 1):  # Loop compares adjacent elements
        if unsorted_list[j] > unsorted_list[j + 1]:  # Checks adjacent elements
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]  # Swaps

print(unsorted_list)  # Output the sorted list
```
### 2.Finding the Longest Common Prefix 
`method 1 `

The program aims to find the longest common prefix among a list of strings, identifying shared leading characters that appear across all strings.


*Logical View:*

1.Initial Assumption: Start with the first string as the presumed common prefix.

2.Sequential Comparison: Iterate through the remaining strings, checking each one against the current prefix.

3.Prefix Adjustment: If a string does not match the prefix, reduce the prefix by removing characters from the end until a match is found or the prefix is empty.

4.Early Termination: If the prefix becomes empty during the process, conclude that no common prefix exists.

5.Output Result: After evaluating all strings, return the longest common prefix found.

```python

def common_prefix(lst):
    prefix = lst[0]  # Assuming the first string is the common prefix

    for string in lst[1:]:  # Looping from the second string in the list
        while not string.startswith(prefix):  # If the current string does not start with the prefix
            prefix = prefix[:-1]  # Shorten the prefix
            if not prefix:  # If prefix becomes empty
                return False  # Return False if there's no common prefix
    return prefix  # Return the prefix or False if it's empty

lst = ['dog', 'door', 'done', 'doing', 'do']
result = common_prefix(lst)
print("Common prefix:", result)
```

`method 2`

The second method enhances efficiency by sorting the list first, then comparing only the first and last strings in the sorted list. This minimizes the number of comparisons needed to find the common prefix, as the largest variations will be at these extremes. This method is generally more efficient than Method 1 because it reduces unnecessary checks for strings that are unlikely to share a prefix.

*Logical View:*

1.Sorting the List: Sort the list of strings to arrange them lexicographically.

2.Identifying Extremes: Focus on the first and last strings in the sorted list.

3.Character Comparison: Compare characters of the first and last strings until a mismatch is found or one string ends.

4.Extracting the Common Prefix: The matched characters form the longest common prefix.

5.Output Result: Return the common prefix or False if no common prefix exists.

```python 

def common_prefix(lst):
    # Step 1: Sort the list
    lst.sort()

    # Step 2: Compare the first and last strings in the sorted list
    first = lst[0]
    last = lst[-1]

    # Step 3: Find the longest common prefix between the first and last strings
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    # Return the common prefix or False if it's empty
    common_prefix = first[:i]
    return common_prefix if common_prefix else False

# Example usage:
lst = ['dog', 'door', 'done', 'doing', 'doooo']
result = common_prefix(lst)
print("Common prefix:", result)
```
### 3.Roman to Integer Conversion

The program aims to convert a string representing a Roman numeral into its corresponding integer value.

*Logical View:*

1.Mapping Values: A dictionary maps each Roman numeral character to its integer value.

2.Initialization: A variable is set to accumulate the total integer value.

3.Iteration: The program iterates through each character in the input string, checking for its validity.

4.Value Addition: If the character is valid, its corresponding integer value is added to the total.


5.Output: After processing all characters, the program returns the accumulated total as the integer equivalent of the Roman numeral.

``` python

def roman_to_int(roman):
    # Define a mapping of Roman numerals to their corresponding integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }

    # Initialize total to 0. This will hold the final sum of the integer value.
    total = 0

    # Iterate over each character (Roman numeral) in the input string
    for i in roman:
        # Check if the character is a valid Roman numeral and present in the dictionary
        if i in roman_values:
            # Add the corresponding integer value to the total
            total += roman_values[i]

    # Return the final sum, which is the integer equivalent of the Roman numeral string
    return total

# Example usage:
# Get a Roman numeral string from the user
roman_str = input("Enter a Roman numeral: ")

# Call the function to convert Roman numeral to integer and store the result
result = roman_to_int(roman_str)

# Output the result to the user
print(f"The integer value of {roman_str} is {result}")

```







