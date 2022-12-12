import numpy as np

moves = {
    'down': np.array((1, 0)),
    'up': np.array((-1, 0)),
    'right': np.array((0, 1)),
    'left': np.array((0, -1))
}

def get_input(file):
    with open(file, 'r') as f:
        grid = []
        lines = list(map(lambda x: x.strip().split(), f.readlines()))
        for i in range(len(lines)):
            grid.append([ord(c) - ord('a') for c in lines[i][0]])
    height_grid = np.array(grid)
    S = tuple(x[0] for x in np.where(height_grid == ord('S') - ord('a')))
    E = tuple(x[0] for x in np.where(height_grid == ord('E') - ord('a')))
    height_grid[S] = 0
    height_grid[E] = 26
    return height_grid, S, E

def can_move(direction, i, j, grid):
    """
    Check if a move from grid[i,j] in specified direction is valid
    meaning it doesn't go out of bounds and the elevation jump is not
    higher than 1 
    """
    point = (i, j)
    new_point = tuple(point + moves[direction])
    return (
        (0 <= new_point[0] < grid.shape[0]) and  # up/down bounds
        (0 <= new_point[1] < grid.shape[1]) and  # left/right bounds
        (grid[point] - grid[new_point] <= 1),  # elevation check
        new_point
    )


def solve(grid, end):
    queue, visited, no_steps = [(end, 0)], set(), {}
    while queue:
        point, lenght = queue.pop(0)
        if point in visited:
            continue
        # get the lenght for cells with elevation 'a'
        if grid[point] == 0:
            no_steps[point] = lenght
        visited.add(point)
        # check every move
        for dir in moves.keys():
            can, new_point = can_move(dir, point[0], point[1], grid)
            if can and (new_point not in visited):
                # we add the node search deeper with increased distance
                queue.append((new_point, lenght+1))
    return no_steps

height_grid, start, end = get_input('input.txt')
lenghts = solve(height_grid, end)
print(f'Part 1: {lenghts[start]}')
print(f'Part 2: {min(lenghts.values())}')
