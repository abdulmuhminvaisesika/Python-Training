def canJump(nums):
    # This will keep track of the farthest index we can reach
    farthest = 0
    
    # Loop through each index of the array
    for i in range(len(nums)):
        # If the current index is not reachable, break out
        if i > farthest:
            return False
        
        # Update the farthest we can reach from index i
        farthest = max(farthest, i + nums[i])
        
        # If we can reach the last index, return True
        if farthest >= len(nums) - 1:
            return True
    
    # If we finish the loop without reaching the last index, return False
    return False

print(canJump([3,2,1,0,4]))  # Output: True





