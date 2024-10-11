# Define the dictionary for brackets
dict_of_brackets = {
    '{': '}',
    '(': ')',
    '[': ']'
}

# Function to check if the string has balanced brackets
def check_bracket_pairs(input_string):
    # First condition: Check if the length of the string is even
    if len(input_string) % 2 != 0:
        return False  # If odd, it can't have matching pairs
    
    stack = []  # Stack to keep track of opening brackets
    
    # Iterate through each character in the string
    for char in input_string:
        # If it's an opening bracket, push it onto the stack
        if char in dict_of_brackets:
            stack.append(char)
        # If it's a closing bracket, check if it matches the last opening bracket
        elif char in dict_of_brackets.values():
            if stack and dict_of_brackets[stack[-1]] == char:
                stack.pop()  # Remove the matching opening bracket from the stack
            else:
                return False  # No match found, return False
    
    # If the stack is empty at the end, all brackets matched correctly
    return len(stack) == 0

# Example usage
input_string = input("enter:")
result = check_bracket_pairs(input_string)

# Output the result
print("Result:", result)
