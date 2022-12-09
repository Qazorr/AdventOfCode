import numpy as np
from pprint import pprint

def get_input(file):
    with open(file, 'r') as f:
        return list(map(lambda x: x.strip().split(), f.readlines()))

def calculate_size(inp):
    x, y, width, height = 0, 0, 0, 0
    for parts in inp:
        match parts[0]:
            case 'R':
                x += int(parts[1])
                width = max(width, x)
            case 'L':
                x -= int(parts[1])
            case 'U':
                y += int(parts[1])
                height = max(height, x)
            case 'D':
                y -= int(parts[1])
    return max(width, height)

def move(direction):
    v = (0, 0)
    match direction:
        case 'R' | 'L':
            v = (0, 1) if direction == 'R' else (0, -1)
        case 'U' | 'D':
            v = (-1, 0) if direction == 'U' else (1, 0)
    return np.array(v)

def move_vector(v):
    return np.array(list(map(np.sign, v)))

def check_adjacency(tail_pos, head_pos):
    v = head_pos - tail_pos
    return (-1 <= v[0] <= 1) and (-1 <= v[1] <= 1), move_vector(v)

lines = get_input('input.txt')
size = 500
visited_grid = np.full((size, size), False)
moves_grid = np.full((size, size), '.')
start = (size//2, size//2)

moves_grid[start] = 's'
tail, head = map(np.array, [start, start])
visited_grid[tail[0], tail[1]] = True

for direction, amount in lines:
    amount = int(amount)
    moves_grid[start] = 's'
    for _ in range(amount):
        moves_grid[head[0], head[1]] = '.'
        moves_grid[tail[0], tail[1]] = '.'
        # print(head, direction, move(direction))
        head += move(direction)
        adj, v = check_adjacency(tail, head)
        if not adj:
            tail += v
            visited_grid[tail[0], tail[1]] = True
        moves_grid[tail[0], tail[1]] = 'T'
        moves_grid[head[0], head[1]] = 'H'

print(visited_grid.sum())