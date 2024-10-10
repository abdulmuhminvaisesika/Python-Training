def roman_to_int(roman):
    # Define a mapping of Roman numerals to their integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    total=0
    for i in roman_str:
        if i in roman_values:
            total+=roman_values[i]
    
    

    return total

# Example usage:
roman_str = input("Enter a Roman numeral: ")
result = roman_to_int(roman_str)
print(f"The integer value of {roman_str} is {result}")

