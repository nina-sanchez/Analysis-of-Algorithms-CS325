# group pseudocode used:
# Function powerset(inputSet):
#     output = []
#     Function backtrack(start, current):
#         output.append(copy of current)
#         for i from start to length of inputSet - 1:
#         current.append(inputSet[i])
#         backtrack(i + 1, current)
#         current.pop()
#         backtrack(0, [])
#         return output


# implementation
def powerset(inputSet):
    output = []
    
    def backtrack(start, current):
        output.append(current[:]) # uses a copy of current
        length = len(inputSet)
        for i in range(start, length):
            current.append(inputSet[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return output


# input = [1, 2, 3]
# print(powerset(input))
