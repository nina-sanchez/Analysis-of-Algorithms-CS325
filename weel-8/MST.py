import heapq

# used this to help https://www.programiz.com/dsa/prim-algorithm

def Prims(G):
    vertices = len(G) # length of graph G
    visited_list = [0] * vertices # list of visited vertices, set to size of vertices
    min_heap = [(0, 0, 0)]  # watches the weight, vertice one , and vertice two

    mst = [] # list of mst that will be returned

    while min_heap:
        # while more, add those to min heap
        weight, vertice_one, vertice_two = heapq.heappop(min_heap)

        # if the vertices were already visited, continue
        if visited_list[vertice_one] and visited_list[vertice_two]:
            continue
        
        # append to list 
        mst.append((vertice_one, vertice_two, weight))
        visited_list[vertice_one] = visited_list[vertice_two] = 1 # switch to 1 as visited in list

        # if has a neighbor, add that neighbor in
        for neighbor_vertice, edge in enumerate(G[vertice_two]):
            if not visited_list[neighbor_vertice] and edge != 0:
                heapq.heappush(min_heap, (edge, vertice_two, neighbor_vertice))
    
    # mine was outputting 0 0 0, so removed it if weight isnt 0 it will print
    removing_start = [(vertice_one, vertice_two, weight) for vertice_one, vertice_two, weight in mst if weight != 0]

    # return the list of enumerated mst edges
    return removing_start

# testing
input = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

running_algo = Prims(input)
print(running_algo)


