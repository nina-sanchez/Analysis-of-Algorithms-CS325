# used this to better understand what i needed to do
# https://www.interviewbit.com/blog/travelling-salesman-problem/

def solve_tsp(G):
    n = len(G) # n is equal to the length of matrix g
    tsp = []
    unvisited = set(range(n))  # this will hold the univisted vertices
    current = 0  # this will hold the current vertice
    tsp.append(current) # begin by appending the first ver
    unvisited.remove(current)
    
    while unvisited: # while there are still unvisited ver
        min_edge = float('inf') 
        next = None # setting next to none
        for neighbor in unvisited: # if there are still unvisited neighbors
            if G[current][neighbor] < min_edge: # if graph is less then min edge
                min_edge = G[current][neighbor]
                next = neighbor # continue
        if next is None:
            break # break once nothing left
        tsp.append(next) # append that ver
        unvisited.remove(next)
        current = next # continue
    # have to then add in the starting vertex to the result tsp
    tsp.append(0)
    return tsp


# TESTING
G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0]
]

testing = solve_tsp(G)
print(testing)
