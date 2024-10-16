# def rotate_array(arr,k):
#     arr_rotated=[]
#     length=len(arr)
#     diff=length-k       #to determine where the split occurs
#     arr_rotated[:]=arr[diff:]+arr[:diff]
#     return arr_rotated
    
    

# print(rotate_array([1, 2, 3, 4, 5], 7))


from typing import List
 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
 
        # Ensure k is within the bounds of the array length
        k = k % len(nums)
 
        # Reverse the entire array
        nums.reverse()
 
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
 
        # Reverse the rest of the array
        nums[k:] = reversed(nums[k:])
        print(nums)
       
 
obj = Solution()
List2 = [1,2,3,4,5,6,7]
obj.rotate(List2,8)