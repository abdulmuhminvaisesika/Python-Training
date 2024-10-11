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
