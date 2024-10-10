def common_prefix(lst):
    

    # Start by assuming the first string is the common prefix
    prefix = lst[0]

    for string in lst[1:]:
        # Reduce the prefix as long as the current string doesn't start with it
        while not string.startswith(prefix):    #If the current string does not start with the prefix, the loop will execute to reduce the prefix.
            prefix = prefix[:-1]  # Shorten the prefix
            if not prefix:  # If prefix becomes empty
                return False  # Return False if there's no common prefix

    return prefix   # Return the prefix or False if it's empty

lst = ['dog', 'door', 'done', 'doing','do']
result = common_prefix(lst)
print("Common prefix:", result)
