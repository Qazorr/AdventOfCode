import numpy as np


class Node:
    def __init__(self, start_v: tuple, label) -> None:
        self.label = label
        self.pos = np.array(start_v)

    def __getitem__(self, key):
        return self.pos[key]

    def move(self, direction):
        v = np.array((0, 0))
        match direction:
            case 'R' | 'L':
                v = np.array((0, 1) if direction == 'R' else (0, -1))
            case 'U' | 'D':
                v = np.array((-1, 0) if direction == 'U' else (1, 0))
            case _:
                pass
        self.pos += v

    def move_to(self, other):
        v = other.pos - self.pos
        if not ((-1 <= v[0] <= 1) and (-1 <= v[1] <= 1)):
            self.pos += np.array(list(map(np.sign, v)))

    def __str__(self) -> str:
        return self.label


class Grid:
    def __init__(self, file, size) -> None:
        self.size = size
        self.start = (self.size//2, self.size//2)
        with open(file, 'r') as f:
            self.lines = list(map(lambda x: x.strip().split(), f.readlines()))
        
        self.visited_grid = np.full((self.size, self.size), False)
        self.moves_grid = np.full((self.size, self.size), '.')
        
        self.moves_grid[self.start] = 's'
        self.visited_grid[self.start] = True

        self.tail = Node(self.start, 'T')
        self.head = Node(self.start, 'H')


    def solve(self):
        for direction, amount in self.lines:
            amount = int(amount)
            self.moves_grid[self.start] = 's'
            for _ in range(amount):
                self.moves_grid[self.head[0], self.head[1]] = '.'
                self.moves_grid[self.tail[0], self.tail[1]] = '.'

                self.head.move(direction)
                self.tail.move_to(self.head)
                self.visited_grid[self.tail[0], self.tail[1]] = True

                self.moves_grid[self.tail[0], self.tail[1]] = str(self.tail)
                self.moves_grid[self.head[0], self.head[1]] = str(self.head)
        return self.visited_grid.sum()


grid = Grid('input.txt', 500)
print(grid.solve())
