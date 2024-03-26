import heapq

# used this to help me 
# https://www.youtube.com/watch?v=XQlxCCx2vI4

def minEffort(puzzle):
    # dimensions of the grid
    rows, cols = len(puzzle), len(puzzle[0]) 
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            puzzle[i][j] # can print this to verify dimensions is correct
    
    # first value is difference, row, and col --> starting at top left corner
    minHeap = [[0, 0, 0]]  # [diff, r, c]
    visited = set() # hash map to note whether already visited or not
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # these are the four diffections
    
    while minHeap:
        # get these three values from minHeap
        difference, r, c = heapq.heappop(minHeap)
        
        if (r, c) in visited:
            continue
        visited.add((r, c)) # add after its popped, to not visit same twice
        if (r, c) == (rows - 1, cols - 1): # if r c == then at the final spot
            return difference # return statement is here instead of at the end
        
        for dr, dc in directions: # for direction in rowor col
            nextRow, nextCol = r + dr, c + dc # new row + col, is adding the directions
            if (nextRow < 0 or nextCol < 0 or # checking and ensuring new row+col, is within bounds 
                nextRow == rows or nextCol == cols or
                (nextRow, nextCol) in visited): # if neighbor has already been visited, then just continue
                continue
            newDiff = max(difference, abs(puzzle[r][c] - puzzle[nextRow][nextCol])) # the new dif is the max of waht we calc and org that we popped
            heapq.heappush(minHeap, [newDiff, nextRow, nextCol]) # 




# TESTING 
# puzzle example 1
# puzzle = [
#     [1, 3, 5],
#     [5, 8, 3],
#     [3, 4, 5]
# ]

# puzzle example 2
# puzzle = [
#     [1, 3, 5],
#     [2, 8, 3],
#     [3, 4, 5]
# ]

# result = minEffort(puzzle)
# print(result)
