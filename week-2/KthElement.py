# Regina Sanchez
# Code using merge sort to combine two sorted arrays
# and find the kth element in the combined array
# The divide step has already been completed so I will be merging them

# adapted code from: https://www.geeksforgeeks.org/merge-two-sorted-arrays/
# as well as from course material

# kthElement(Arr1, Arr2, k)
# example: 
# Arr1 = [1,2,3,5,6] ; Arr2= [3,4,5,6,7] ; k= 5
# Returns: 4
  
def kthElement(Arr1, Arr2, k):
    size_arr1 = len(Arr1)
    size_arr2 = len(Arr2)
    
    Arr3 = [0] * (size_arr1 + size_arr2)  # initializing empty array size of merged arrays
   
    # initializing values
    i = 0
    j = 0
    m = 0
    
    # looping through both arrays
    while i < size_arr1 and j < size_arr2:
        if Arr1[i] < Arr2[j]: # picking which array has lowest value 
            Arr3[m] = Arr1[i]
            m += 1
            i += 1
        else:
            Arr3[m] = Arr2[j]
            m += 1
            j += 1
    while i < size_arr1:    # puts rest of elements from Arr1 into the merged array
        Arr3[m] = Arr1[i]
        m += 1
        i += 1
        
    while j < size_arr2:    # puts the rest of the elemnts from Arr 2 into the merged array
        Arr3[m] = Arr2[j]
        m += 1
        j += 1
    
    return Arr3[k - 1]
    #return print("Kth element:", Arr3[k - 1]) # returns kth element of merged array --> Arr3
        
        
# driver from homework
# Arr1 = [1,2,3,5,6]
# Arr2 = [3,4,5,6,7]
# k = 5
# kthElement(Arr1, Arr2, k)
