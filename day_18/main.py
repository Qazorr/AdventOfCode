def parse(file):
    cubes = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            cubes.append(tuple(map(int, line.split(','))))
    return sorted(cubes, key=lambda x: (x[0], x[1], x[2]))

def inclusive_range(start, stop, step=1):
    return range(start, stop+step, step)

def neighbours(x, y, z):
    return (
        (x-1, y, z),
        (x+1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1)
    )

def part1(cubes):
    visited = set()
    surface = 0
    for cube in cubes:
        visited.add(cube)
        for xx in inclusive_range(cube[0]-1, cube[0]+1):
            if (xx, cube[1], cube[2]) not in visited:
                surface += 1
            elif xx != cube[0]:
                surface -= 1
        for yy in inclusive_range(cube[1]-1, cube[1]+1):
            if (cube[0], yy, cube[2]) not in visited:
                surface += 1
            elif yy != cube[1]:
                surface -= 1
        for zz in inclusive_range(cube[2]-1, cube[2]+1):
            if (cube[0], cube[1], zz) not in visited:
                surface += 1
            elif zz != cube[2]:
                surface -= 1
    return surface

def part2(cubes):
    min_cube, max_cube = [min(x)-1 for x in zip(*cubes)
                          ], [max(x)+1 for x in zip(*cubes)]
    visited, queue = set(cubes), [tuple(min_cube)]
    surface = 0
    while queue:
        for cube in neighbours(*queue.pop(0)):
            if all(a <= x <= b for a, x, b in zip(min_cube, cube, max_cube)):
                surface += cube in cubes
                if cube not in visited:
                    visited.add(cube)
                    queue.append(cube)
    return surface

cubes = parse('input.txt')
print(part1(cubes))
print(part2(cubes))
