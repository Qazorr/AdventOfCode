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
    def __init__(self, file, size, no_knots=9, get_moves_grid=False) -> None:
        self.size = size
        self.start = (self.size//2, self.size//2)
        self.get_moves_grid = get_moves_grid
        with open(file, 'r') as f:
            self.lines = list(map(lambda x: x.strip().split(), f.readlines()))
        self.visited_grid = np.full((self.size, self.size), False)
        
        if(self.get_moves_grid):
            self.moves_grid = np.full((self.size, self.size), '.')
            self.moves_grid[self.start] = 's'

        self.head = Node(self.start, 'H')
        self.knots = [Node(self.start, f'{i}') for i in range(1, no_knots+1)]
        self.knots.insert(0, self.head)

        self.visited_grid[self.start] = True

    def solve(self) -> int:
        for direction, amount in self.lines:
            amount = int(amount)
            if (self.get_moves_grid): self.moves_grid[self.start] = 's'
            for _ in range(amount):
                if (self.get_moves_grid):
                    for knot in self.knots:
                        self.moves_grid[knot[0], knot[1]] = '.'
                
                self.knots[0].move(direction)
                for idx, knot in enumerate(self.knots[1:], start=1):
                    knot.move_to(self.knots[idx-1])
                self.visited_grid[self.knots[-1][0], self.knots[-1][1]] = True
                
                if (self.get_moves_grid):
                    for knot in self.knots[::-1]:
                        self.moves_grid[knot[0], knot[1]] = str(knot)

        return self.visited_grid.sum()


# should think about how to calculate the grid size
print(f'Part 1:', Grid('input.txt', 500, no_knots=1).solve())
print(f'Part 2:', Grid('input.txt', 500, no_knots=9).solve())
