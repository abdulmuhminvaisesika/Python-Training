def rotate_array(arr,k):
    arr_rotated=[]
    length=len(arr)
    diff=length-k
    arr_rotated[:]=arr[diff:]+arr[:diff]
    return arr_rotated
    
    

print(rotate_array([1, 2, 3, 4, 5], 3))

