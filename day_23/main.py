from collections import defaultdict

def parse(file):
    elves = set()
    with open(file, 'r') as f:
        for y, row in enumerate(f.readlines()):
            for x, col in enumerate(row):
                if col == '#': elves.add(x+(y*1j))
    return elves

directions = [
        # e.g ((north, north-east, north-west), north)
        ((-1j, 1-1j, -1-1j), -1j),  # N
        (( 1j, 1+1j, -1+1j),  1j),  # S
        ((-1, -1+1j, -1-1j), -1),   # W
        (( 1,  1+1j,  1-1j),  1)    # E
]  

can_move = lambda elves, elf, where: all([(elf + direction) not in elves for direction in where])

def solve(elves, end=10):
    moves, round = 1, 0
    neighbours = set([d for n, _ in directions for d in n])
    while moves:
        if round == end:
            x, y = [pos.real for pos in elves], [pos.imag for pos in elves]
            part1 = int((max(x) - min(x) + 1) * (max(y) - min(y) + 1) - len(elves))
        next = defaultdict(list)
        for elf in elves:
            if can_move(elves, elf, neighbours): continue
            for steps, direction in directions:
                if can_move(elves, elf, steps):
                    next[elf+direction].append(elf)
                    break
        moves = 0
        for next_pos, cur_pos in next.items():
            if len(cur_pos) == 1:
                elves.remove(cur_pos[0])
                elves.add(next_pos)
                moves += 1
        directions.append(directions.pop(0))
        round += 1
    return part1, round

if __name__ == "__main__":
    p1, p2 = solve(parse('input.txt'))
    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')