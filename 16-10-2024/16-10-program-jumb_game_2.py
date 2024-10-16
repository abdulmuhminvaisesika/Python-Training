def jump(nums):
    # Initialize the number of jumps, current end of the jump, and farthest point we can reach
    jumps = 0
    current_end = 0
    farthest = 0
    
    # Loop through the array except for the last element
    for i in range(len(nums) - 1):
        # Update the farthest we can reach from the current index
        farthest = max(farthest, i + nums[i])
        
        # If we reach the end of the current jump range
        if i == current_end:
            # Increment the jump count
            jumps += 1
            # Update the current jump end to the farthest we can reach
            current_end = farthest
            
    return jumps
print(jump([2,1,2,1,4]))
