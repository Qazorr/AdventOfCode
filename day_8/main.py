import numpy as np

def parse(file):
    with open(file, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    for i in range(len(lines)):
        lines[i] = np.array(list(map(int, [c for c in lines[i]])))
    return np.array(lines)

def part1(height_grid):
    visibility_grid = np.full(height_grid.shape, False)
    
    # 90 deg * 4 = 360 deg
    for _ in range(4):
        visibility_grid[:, 0] = True # mark first outer column as visible
        
        # [3 0 3 7 3] -> [3 3 3 7 7]
        maximum_grid = np.maximum.accumulate(height_grid, 1)
        
        # fill other columns depending on whether they are higher than current maximum
        visibility_grid[:, 1:] |= height_grid[:, 1:] > maximum_grid[:, :-1]
        
        # rotate 90 degrees to go through all possibilities (top, right, bottom, left)
        height_grid, visibility_grid = map(np.rot90, [height_grid, visibility_grid]) 
    return visibility_grid.sum()
    

def part2(height_grid):
    rotations = 4
    num_visible = np.full((*height_grid.shape, rotations), 0)
    
    # 90 deg * 4 = 360 deg
    for rot in range(rotations):
        for (j, i), value in np.ndenumerate(height_grid):
            can_see = 0
            for x in range(i-1, -1, -1):
                can_see += 1
                # got the tree that blocks the vision
                if height_grid[j, x] >= value:
                    break
            num_visible[j, i, rot] = can_see

        # rotate 90 degrees to go through all possibilities (top, right, bottom, left)
        height_grid, num_visible = map(np.rot90, [height_grid, num_visible])
    return num_visible.prod(2).max()

if __name__ == "__main__":
    inp = parse('input.txt')
    print(part1(inp))
    print(part2(inp))