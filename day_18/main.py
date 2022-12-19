inclusive_range = lambda start, stop, step=1: range(start, stop+step, step)

def parse(file):
    cubes = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            cubes.append(tuple(map(int, line.split(','))))
    return sorted(cubes, key=lambda x: (x[0], x[1], x[2]))

def part1(cubes):
    v = set()
    surface = 0
    for cube in cubes:
        v.add(cube)
        for xx in inclusive_range(cube[0]-1, cube[0]+1):
            if (xx, cube[1], cube[2]) not in v: surface += 1
            elif xx != cube[0]: surface -= 1 
        for yy in inclusive_range(cube[1]-1, cube[1]+1):
            if (cube[0], yy, cube[2]) not in v: surface += 1
            elif yy != cube[1]: surface -= 1
        for zz in inclusive_range(cube[2]-1, cube[2]+1):
            if (cube[0], cube[1], zz) not in v: surface += 1
            elif zz != cube[2]: surface -= 1
    return surface

print(part1(parse('input.txt')))