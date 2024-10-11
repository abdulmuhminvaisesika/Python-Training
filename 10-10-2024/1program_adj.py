# Define the dictionary for brackets
dict_of_brackets = {
    '{': '}',
    '(': ')',
    '[': ']'
}

# Function to check if the string has balanced brackets using adjacent pair removal
def check_bracket_pairs(input_string):
    # First condition: Check if the length of the string is even
    if len(input_string) % 2 != 0:
        return False  # If odd, it can't have matching pairs

    # Keep iterating until no more adjacent pairs can be removed
    while True:
        initial_length = len(input_string)
        
        # Replace any adjacent valid pairs with an empty string
        for key, value in dict_of_brackets.items():
            input_string = input_string.replace(f"{key}{value}", "")
        
        # If no more characters were removed, break the loop
        if len(input_string) == initial_length:
            break
    
    # If the string is empty, all brackets matched
    return len(input_string) == 0

# Example usage
input_string = input("Enter a string of brackets: ")
result = check_bracket_pairs(input_string)

# Output the result
print("Result:", result)
