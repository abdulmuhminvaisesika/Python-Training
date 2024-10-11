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
