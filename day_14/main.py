moves = {
    'down': (0, 1),
    'up': (0, -1),
    'right': (1, 0),
    'left': (-1, 0)
}

def parse(file):
    with open(file, 'r') as f:
        lines = list(map(lambda x: x.strip().split(), f.readlines()))
        for i in range(len(lines)):
            lines[i] = list(filter(lambda x: x != '->', lines[i]))
    return lines

def get_line(x1, y1, x2, y2):
    line = set()
    if x1 == x2:
        for y in range(min(y1, y2), max(y1,y2)+1):
            line.add((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            line.add((x, y1))
    return line    

def interpret(lines):
    rocks = set()
    for line in lines:
        for i in range(len(line)-1):
            x1, y1 = tuple(map(int, line[i].split(',')))
            x2, y2 = tuple(map(int, line[i+1].split(',')))
            rocks |= get_line(x1, y1, x2, y2)
    return rocks

add_move = lambda point, v: (point[0] + v[0], point[1] + v[1])
move = lambda dir, point: add_move(point, moves[dir])

def fall(rocks, sand, max_y):
    particle = sand
    for _ in range(0, max_y):
        if (new := move('down', particle)) not in rocks:
            particle = new
        elif (new := move('left', move('down', particle))) not in rocks:
            particle = new
        elif (new := move('right', move('down', particle))) not in rocks:
            particle = new
        else:
            return particle
    return particle
            
def part1(rocks, start):
    max_y = max(rocks, key=lambda x: x[1])[1]
    count = 0
    while(True):
        solution = fall(rocks, start, max_y)
        if solution[1] >= max_y:
            return count
        rocks |= {(solution)}
        count += 1

def part2(rocks, start):
    max_y = max(rocks, key=lambda x: x[1])[1] + 1
    count = 0
    while (True):
        solution = fall(rocks, start, max_y)
        rocks |= {(solution)}
        count += 1
        if solution == start:
            return count

start = (500, 0)
print(part1(interpret(parse('input.txt')), start))    
print(part2(interpret(parse('input.txt')), start))
