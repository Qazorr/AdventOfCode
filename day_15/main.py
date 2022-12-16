from pprint import pprint

SOLUTION1 = 5073496
SOLUTION2 = 16120878617600

def parse(file):
    with open(file, 'r') as f:
        to_return = []
        lines = list(map(lambda x: x.strip().split(), f.readlines()))
        for line in lines:
            to_return.append([x[2:] for x in line if x[0] in ['x', 'y']])
        for i in range(len(to_return)):
            for j in range(4):
                to_return[i][j] = int(to_return[i][j][:-1]) if to_return[i][j][-1] in [',', ':'] else int(to_return[i][j])
    return to_return

manhattan = lambda p, q: (abs(p[0] - q[0]), abs(p[1] - q[1]))

def interpret(lines):
    for i in range(len(lines)):
        xS, yS, xB, yB = lines[i]
        S, B = (xS, yS), (xB, yB)
        lines[i] = [S, B, manhattan(S, B)]

def part1(interpreted_lines, y):
    rs = []
    beacons = set()
    for line in interpreted_lines:
        S, B, diff = line
        if B[1] == y:
            beacons.add(B[0])
        ab = diff[0] + diff[1]
        dy = abs(S[1] - y)
        steps = ab - dy
        if steps > 0:
            rs.append(list(range(S[0]-steps, S[0]+steps+1)))

    output = set()
    for r in rs:
        output |= set(r)
    output -= beacons
    return output
def sum_ranges(r1, r2, bottom, top):
    return (max(min(r1[0], r2[0]), bottom), min(max(r1[1], r2[1]), top))        

def merge(intervals, bounds):
    tmp = intervals[0]
    for interval in intervals:
        if interval[0] <= tmp[1]:
            tmp = (tmp[0], max(tmp[1], interval[1]))
        else:
            return (max(tmp[0], bounds[0]), min(tmp[1], bounds[1]))
    return (max(tmp[0], bounds[0]), min(tmp[1], bounds[1]))

def part2(interpreted_lines, y_max):
    rs = []
    for i in range(y_max):
        rs.append([])
        for line in interpreted_lines:
            S, B, diff = line
            ab = diff[0] + diff[1]
            dy = abs(S[1] - i)
            steps = ab - dy
            if steps > 0:
                rs[i].append((S[0]-steps, S[0]+steps))
        rs[i] = merge(sorted(rs[i]), (0, 4_000_000))
    for i, r in enumerate(rs):
        if r[1] != 4_000_000:
            return i+((r[1]+1)*4_000_000)
    
interpret(lines := parse('input.txt'))
print(len(part1(lines, 2_000_000)))
print(part2(lines, 4_000_000))
