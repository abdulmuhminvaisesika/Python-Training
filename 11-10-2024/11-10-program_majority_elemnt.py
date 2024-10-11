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
a = [1,2,2,1,1,1,1]
output = find_most_frequent_elements(a)
print(output)
