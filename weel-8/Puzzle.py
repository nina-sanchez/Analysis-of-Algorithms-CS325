def solve_puzzle(Board, Source, Destination):
    num_rows, num_cols = len(Board), len(Board[0])
    queue = [(Source, [Source], "")]
    visited = set()
    moves = [(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]

    while queue:
        # will add to visited set to track them
        (curr_row, curr_col), path, curr_direction = queue.pop(0)
        visited.add((curr_row, curr_col))

        # if the row + col + end point then return how it got there
        if (curr_row, curr_col) == Destination:
            return path, curr_direction

        # for available moves, will get the new position in puzzle
        for (row_move, col_move, move_name) in moves:
            new_row, new_col = curr_row + row_move, curr_col + col_move
            new_pos = (new_row, new_col)
            
            # if they are greater than 0 and less than the num of rows and cols, keeps in board
            if (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                # and not # which means cant be on
                if (new_pos not in visited and Board[new_row][new_col] != '#'):
                    # will append that new path as well as the move used --> xtra credit
                    queue.append((new_pos, path + [new_pos], curr_direction + move_name))

    return None

# testing:
Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

start_point = (0, 2)
end_point = (2, 2)
print(solve_puzzle(Puzzle, start_point, end_point))

start_point2 = (0, 0)
end_point2 = (4, 4)
print(solve_puzzle(Puzzle, start_point2, end_point2))

start_point3 = (0, 0)
end_point3 = (4, 0)
print(solve_puzzle(Puzzle, start_point3, end_point3))

start_point4 = (0, 0)
end_point4 = (0, 0)
print(solve_puzzle(Puzzle, start_point4, end_point4))


