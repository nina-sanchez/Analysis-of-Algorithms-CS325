# took inspiration from: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# as well as from the class module: 
# https://canvas.oregonstate.edu/courses/1971181/pages/exploration-3-dot-3-dynamic-programming-longest-common-subsequence-problem?module_item_id=23982921

def dna_match_bottomup(DNA1, DNA2):
    n = len(DNA2)
    m = len(DNA1)
    memoryTable = [[None]*(n + 1) for i in range(m + 1)] # beging with tabulation
    for i in range(m + 1):  # looping through lengths
        for j in range(n + 1):
            if i == 0 or j == 0:  # base case
                memoryTable[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]: # if they match
                memoryTable[i][j] = (memoryTable[i - 1][j - 1] + 1)
            else:
                memoryTable[i][j] = max(memoryTable[i - 1][j], memoryTable[i][j - 1])
    return memoryTable[m][n]  # returns the length of the longest string


def topdown_helper(DNA1, DNA2, m, n, memory):
    if m == 0 or n == 0: # base
        return 0
    if memory[m][n] < 0:  # if it is not in mem
        if DNA1[m - 1] == DNA2[n - 1]:  # if match
            memory[m][n] = 1 + topdown_helper(DNA1, DNA2, m - 1, n - 1, memory)
        else:
            memory[m][n] = max(topdown_helper(DNA1, DNA2, m, n - 1, memory), topdown_helper(DNA1, DNA2, m - 1, n, memory)) # if dont match take last max
    return memory[m][n]
    
def dna_match_topdown(DNA1, DNA2):
    m = len(DNA1) # getting lengths
    n = len(DNA2)
    memory = [[-1] * (n + 1) for _ in range(m + 1)] # creating mem for memoization
    
    return topdown_helper(DNA1, DNA2, m, n, memory)
            

# run code
# DNA1 = "ATAGGTAGGATAGAT"
# DNA2 = "GTGAATTTAGTAGTAAA"
# print("bottom-up: ", dna_match_bottomup(DNA1, DNA2))
# print("top-down: ", dna_match_topdown(DNA1, DNA2))

