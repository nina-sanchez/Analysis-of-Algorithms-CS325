# referenced this to remove my repeating outputs: 
# https://www.geeksforgeeks.org/python-removing-duplicates-from-tuple/

def amount_helper(A, start, result, remainder, array):
    length = len(A) # length of list A
    # base case
    if (remainder == 0): # if it equals target sum
        result.add(tuple(sorted(array))) # had to use tuple bc hashing / duplicate errors
    for i in range(start, length): # iterate from beginning to end of list A
        array.append(A[i]) # add elements from list A to array
        amount_helper(A[:i] + A[i+1:], 0, result, remainder - A[i], array) # recursive
        array.pop() # if hits base pop
    return result # returns the result 

def amount(A, S):
    result = set() # result is set to a set()
    final = amount_helper(A, 0, result, S, []) # calls helper
    final_output = [] # setting final output to empty set
    for array in final: # converts the tuple to list
        final_output.append(list(array))
    return final_output

# testing
# A = [11,1,3,2,6,1,5]
# S = 8
# # Result = [[1, 1, 1]]
# print(amount(A, S))