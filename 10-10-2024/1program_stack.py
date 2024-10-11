# Define the dictionary for brackets
dict_of_brackets = {
    '{': '}',
    '(': ')',
    '[': ']'
}

# Function to check if the string has balanced brackets using stack concept
def check_bracket_pairs(input_string):
    if len(input_string) % 2 != 0:        
        return False  # Check if the length is even

    stack = []  # Stack to keep track of opening brackets

    for char in input_string:
        if char in dict_of_brackets:  # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in dict_of_brackets.values():  # If it's a closing bracket
            if not stack or dict_of_brackets[stack[-1]] != char:  # Check if it matches the last opening bracket
                return False
            stack.pop()  # If it's a match, pop the last opening bracket from the stack

    return len(stack) == 0  # Return True if the stack is empty (all brackets matched)

# Example usage
input_string = input("Enter: ")
result = check_bracket_pairs(input_string)

# Output the result
print("Result:", result)
