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
