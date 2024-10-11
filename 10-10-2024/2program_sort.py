unsorted_list = [2,10, 3,4, 5, 7, 1, 8]

for i in range(len(unsorted_list)): #loop runs each element in the list # each iteartion higest elements bubles top 
    for j in range(0, len(unsorted_list) - i - 1):     #loop compare adjacent elements and perform swapping
                    #Each pass of the outer loop reduces the range of unsorted elements. 

        if unsorted_list[j] > unsorted_list[j + 1]:    #checks adjecnt elemets 
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]    #swaps

print(unsorted_list)     
